# LazySnaffler

A cross-platform Python tool to parse Snaffler logs and generate beautiful, interactive HTML dashboards for loot analysis with advanced UI/UX features.

![LazySnaffler Dashboard](https://github.com/QwesiRED/LazySnaffler/raw/main/dashboard-screenshot.png)

## Features
- **Snaffler Log Parsing**: Extracts findings from Snaffler log files
- **CSV Generation**: Outputs structured CSV data for dashboard consumption
- **Three Modes**:
  - `--http` : Serve dashboard and CSV via local HTTP server (auto-loads CSV)
  - `--offline` : Generate HTML with embedded CSV (no server needed)
  - `--manual` (default): Output CSV and print instructions for manual upload
- **Cross-platform**: Works on Windows, macOS, and Linux
- **No Dependencies**: Uses only Python standard library
- **All processing is local**—no data leaves your machine

## Requirements
- Python 3.7+
- Standard library only (no extra pip packages required)
- A modern web browser (Chrome, Edge, Firefox, Safari)

## Usage
1. Place your Snaffler log (e.g. `ExampleData/snafflerlog.txt`) in the ExampleData directory.
2. Run the tool:

### Manual mode (default)
```
python lazysnaffler.py -f ExampleData/snafflerlog.txt
```
- Open `Template.html` in your browser
- Click 'browse' and select the generated CSV file

### HTTP server mode (auto-loads CSV)
```
python lazysnaffler.py -f ExampleData/snafflerlog.txt --http
```
- The dashboard will open in your browser and load the CSV automatically

### Offline mode (HTML with embedded CSV)
```
python lazysnaffler.py -f ExampleData/snafflerlog.txt --offline
```
- The tool generates `Template_offline.html` and opens it in your browser

## Dashboard Features
The generated dashboard includes:
- **Interactive Data Table**: Sortable, filterable table with column visibility controls
- **Review System**: Mark findings as reviewed/pending with persistent status
- **Multiple Export Options**: CSV, Excel, PDF export capabilities
- **Real-time Filtering**: Global search and column-specific filters
- **Statistics Dashboard**: Charts and metrics for data analysis
- **Settings Panel**: Theme customization, chart types, and data management

*For detailed dashboard documentation, see the [Wiki](https://github.com/QwesiRed/LazySnaffler/wiki)*

## Files
- `lazysnaffler.py` — Main Python script
- `Template.html` — Advanced HTML dashboard template with AdminLTE
- `ExampleData/snafflerlog.txt` — Sample Snaffler log file
- `README.md` — This file

## Technology Stack
- **Backend**: Python 3.7+ (standard library only)
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: AdminLTE 3.x
- **Data Tables**: DataTables with Bootstrap 5
- **Charts**: Chart.js
- **Icons**: FontAwesome
- **Export**: jsPDF, html2canvas, PapaParse

## Author
**QwesiRed**
- GitHub: [@QwesiRed](https://github.com/QwesiRed)
- LinkedIn: [QwesiRed](https://linkedin.com/in/qwesired)
- Twitter: [@QwesiRed](https://twitter.com/qwesired)

## License
This project is open source and available under the MIT License.
