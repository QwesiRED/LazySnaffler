# Frequently Asked Questions (FAQ)

## General Questions

### What is LazySnaffler?
LazySnaffler is a Python tool that parses Snaffler log files and generates an interactive HTML dashboard for analyzing loot findings. It provides a modern web interface with filtering, review capabilities, and export options.

### What is Snaffler?
Snaffler is a tool for finding sensitive information in Active Directory environments. It scans for files containing passwords, credentials, and other sensitive data.

### Is LazySnaffler free?
Yes, LazySnaffler is open source and free to use under the MIT License.

### What operating systems are supported?
LazySnaffler works on Windows, macOS, and Linux. It only requires Python 3.7+ and uses the standard library.

## Installation and Setup

### How do I install LazySnaffler?
1. Download the repository
2. Ensure Python 3.7+ is installed
3. No additional packages are required
4. Run the script with your Snaffler log file

### Do I need to install any Python packages?
No, LazySnaffler uses only the Python standard library. No pip packages are required.

### What Python version do I need?
Python 3.7 or higher is required.

### Can I run it without internet access?
Yes, the offline mode generates a self-contained HTML file with embedded data that works without internet access.

## Usage Questions

### How do I run LazySnaffler?
```bash
# Basic usage
python lazysnaffler.py -f ExampleData/snafflerlog.txt

# HTTP server mode (auto-loads data)
python lazysnaffler.py -f ExampleData/snafflerlog.txt --http

# Offline mode (embedded data)
python lazysnaffler.py -f ExampleData/snafflerlog.txt --offline
```

### What file formats are supported?
LazySnaffler reads Snaffler log files (text format) and outputs CSV data for the dashboard.

### Can I use it with other tools?
Yes, the generated CSV can be imported into other analysis tools, and the dashboard can export data in multiple formats.

## Dashboard Questions

### What browsers are supported?
Modern browsers including Chrome, Edge, Firefox, and Safari are supported.

### Can I use it on mobile devices?
Yes, the dashboard is responsive and works on tablets and mobile devices.

### How do I upload my data?
1. Run the Python script to generate CSV
2. Open the dashboard in your browser
3. Click "Browse" and select the CSV file
4. The data will load automatically

### Can I save my work?
Yes, the dashboard saves your review status and settings in browser localStorage.

## Data and Privacy

### Is my data sent anywhere?
No, all processing is local. Your data never leaves your machine.

### Where is my data stored?
- CSV files are stored locally
- Dashboard data is stored in browser localStorage
- No cloud storage is used

### Can I clear my data?
Yes, use the "Clear All Data" option in Settings to remove all loaded data.

### Is the data encrypted?
No, the data is stored in plain text. Use appropriate security measures for sensitive data.

## Features and Functionality

### How do I mark items as reviewed?
Click the checkbox in the Actions column. The item will show as "Reviewed" with a green badge.

### Can I filter by review status?
Yes, use the Status filter dropdown to show only Reviewed or Pending items.

### How do I export my data?
Use the export buttons (Copy, CSV, Excel, PDF) in the action bar. Only filtered/visible data is exported.

### Can I hide columns?
Yes, use the "Show/Hide Columns" button to toggle column visibility.

### How do I search for specific items?
Use the global search field at the top of the table to search across all columns.

### Can I change the theme?
Yes, go to Settings and choose between Light and Dark themes.

## Troubleshooting

### The dashboard won't load
- Check that JavaScript is enabled
- Try a different browser
- Ensure the HTML file is accessible
- Check browser console for errors

### My data isn't showing
- Verify the CSV file format
- Check that the file was uploaded correctly
- Ensure the data contains the expected columns
- Try refreshing the page

### Export isn't working
- Check that data is loaded
- Verify browser download permissions
- Try a different export format
- Check browser console for errors

### Review status is lost
- Check browser localStorage settings
- Ensure JavaScript is enabled
- Verify you haven't cleared browser data
- Check if new data was loaded (resets review status)

### Performance is slow
- Reduce the number of visible columns
- Use filters to limit data size
- Clear old data regularly
- Try a different browser

### Charts aren't displaying
- Check that JavaScript is enabled
- Verify Chart.js is loading
- Check browser console for errors
- Try refreshing the page

## Advanced Questions

### Can I customize the dashboard?
Yes, you can modify the HTML template, but this requires web development knowledge.

### Can I integrate with other tools?
The CSV output can be imported into other tools, and the dashboard can export data in multiple formats.

### Is there an API?
No, LazySnaffler is a standalone tool with no API.

### Can I contribute to the project?
Yes, contributions are welcome. Check the GitHub repository for contribution guidelines.

### How do I report bugs?
Report bugs through the GitHub repository's issue tracker.

### Can I request new features?
Yes, feature requests can be submitted through the GitHub repository's issue tracker.

## Security Questions

### Is it safe to use on sensitive data?
Yes, all processing is local and no data is transmitted. However, ensure appropriate security measures for your environment.

### Should I use it on production systems?
Use appropriate caution and follow your organization's security policies.

### Can I use it in air-gapped environments?
Yes, the offline mode generates self-contained HTML files that work without internet access.

### Are there any security vulnerabilities?
The tool uses standard web technologies. Keep your browser updated and follow security best practices.

## Performance Questions

### How much data can it handle?
Performance depends on your system and browser. Large datasets (10,000+ items) may be slower.

### Can I improve performance?
- Hide unused columns
- Use filters to reduce data size
- Clear old data regularly
- Use a modern browser

### Does it work with very large files?
Yes, but performance may be slower. Consider filtering data before analysis.

### How much memory does it use?
Memory usage depends on data size and browser. Modern browsers handle large datasets well.

## Support and Community

### Where can I get help?
- Check this FAQ
- Review the wiki documentation
- Search GitHub issues
- Create a new issue for bugs or questions

### Is there a community?
The GitHub repository serves as the community hub for discussions and support.

### How often is it updated?
Updates are released as needed. Check the GitHub repository for the latest version.

### Who maintains the project?
The project is maintained by QwesiRed and the community.
