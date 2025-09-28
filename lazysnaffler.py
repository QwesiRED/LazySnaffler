# lazysnaffler - Snaffler log parser and dashboard loader
# Author: QwesiRed

BANNER = '=== LazySnaffler ==='

import argparse
import csv
import os
import re
import sys
import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading

def print_banner():
    print(BANNER)

def parse_snaffler_log(log_path):
    rows = []
    with open(log_path, encoding='utf-8', errors='replace') as f:
        for line in f:
            if '\t[File]\t' in line:
                parts = line.strip().split('\t')
                try:
                    idx = parts.index('[File]')
                except ValueError:
                    continue
                
                # Extract user@computer and timestamp from the beginning of the line
                user_computer = ''
                timestamp = ''
                if len(parts) > 0:
                    # First part contains [user@computer]
                    user_computer = parts[0]
                if len(parts) > 1:
                    # Second part contains timestamp
                    timestamp = parts[1]
                
                # Map fields according to Snaffler log format
                severity = parts[idx+1] if len(parts) > idx+1 else ''
                rule = parts[idx+2] if len(parts) > idx+2 else ''
                permission = parts[idx+3] if len(parts) > idx+3 else ''
                keyword = parts[idx+6] if len(parts) > idx+6 else ''
                file_size = parts[idx+7] if len(parts) > idx+7 else ''
                modified = parts[idx+8] if len(parts) > idx+8 else ''
                unc = parts[idx+9] if len(parts) > idx+9 else ''
                
                # Extract file extension from UNC path
                extension = ''
                if unc:
                    m = re.search(r'(\.[A-Za-z0-9]+)$', unc)
                    extension = m.group(1) if m else ''
                
                # Content is everything after the UNC path
                content = parts[idx+10] if len(parts) > idx+10 else ''
                
                rows.append({
                    'timestamp': timestamp,
                    'user_computer': user_computer,
                    'severity': severity,
                    'rule': rule,
                    'permission': permission,
                    'keyword': keyword,
                    'file_size': file_size,
                    'modified': modified,
                    'extension': extension,
                    'unc': unc,
                    'content': content
                })
    return rows

def write_csv(rows, csv_path):
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'timestamp', 'user_computer', 'severity', 'rule', 'permission', 
            'keyword', 'file_size', 'modified', 'extension', 'unc', 'content'
        ])
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def serve_dashboard(html_path, csv_path, port=8000):
    with open(html_path, encoding='utf-8') as f:
        html = f.read()
    inject = '''
    <script>
    window.addEventListener('DOMContentLoaded', function() {
      fetch('lazysnaffler_loot.csv').then(r=>r.blob()).then(blob=>{
        const file = new File([blob], 'lazysnaffler_loot.csv', {type:'text/csv'});
        handleFile(file);
      });
    });
    </script>
    '''
    html = html.replace('</body>', inject + '\n</body>')
    temp_html = 'lazysnaffler_dashboard_autoload.html'
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html)
    class Handler(SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.path = '/' + temp_html
            return super().do_GET()
    server = ThreadedHTTPServer(('localhost', port), Handler)
    print(f"Serving lazysnaffler dashboard at http://localhost:{port}/ ... (Ctrl+C to stop)")
    threading.Timer(1.0, lambda: webbrowser.open(f'http://localhost:{port}/')).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        if os.path.exists(temp_html):
            os.remove(temp_html)

def embed_csv_in_html(html_path, csv_path, output_html):
    with open(html_path, encoding='utf-8') as f:
        html = f.read()
    with open(csv_path, encoding='utf-8') as f:
        csv_data = f.read().replace('\\', '\\\\').replace('`', '\\`')
    inject = f'''
    <script>
    window.addEventListener('DOMContentLoaded', function() {{
      const csvData = `{csv_data}`;
      const blob = new Blob([csvData], {{type:'text/csv'}});
      const file = new File([blob], 'lazysnaffler_loot.csv', {{type:'text/csv'}});
      handleFile(file);
    }});
    </script>
    '''
    html = html.replace('</body>', inject + '\n</body>')
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    print_banner()
    parser = argparse.ArgumentParser(description='lazysnaffler: Parse Snaffler log and output dashboard CSV (with HTML dashboard integration).')
    parser.add_argument('-f', '--file', default='ExampleData/snafflerlog.txt', help='Path to snafflerlog.txt')
    parser.add_argument('--http', action='store_true', help='Serve dashboard and CSV via local HTTP server (auto-loads CSV)')
    parser.add_argument('--offline', action='store_true', help='Generate HTML with embedded CSV (no server needed)')
    parser.add_argument('--html', default='Template.html', help='Path to dashboard HTML template')
    parser.add_argument('--csv', default='lazysnaffler_loot.csv', help='Output CSV filename')
    args = parser.parse_args()

    rows = parse_snaffler_log(args.file)
    if not rows:
        print('No [File] entries found in log.')
        sys.exit(1)
    write_csv(rows, args.csv)
    print(f'CSV written to {args.csv}')

    if args.http:
        serve_dashboard(args.html, args.csv)
    elif args.offline:
        output_html = 'lazysnaffler_dashboard_offline.html'
        embed_csv_in_html(args.html, args.csv, output_html)
        print(f'Offline HTML written to {output_html}')
        webbrowser.open('file://' + os.path.abspath(output_html))
    else:
        print('\nManual mode:')
        print(f'1. Open {args.html} in your browser.')
        print(f'2. Click "browse" and select {args.csv} to load your data.')
        print('\nExample usage:')
        print('  python lazysnaffler/lazysnaffler.py --http')
        print('  python lazysnaffler/lazysnaffler.py --offline')
        print('  python lazysnaffler/lazysnaffler.py -f ExampleData/snafflerlog.txt --http')

if __name__ == '__main__':
    main()
