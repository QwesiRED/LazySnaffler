# Export Options

LazySnaffler provides multiple export options to help you create reports and share your analysis results.

## Available Export Formats

### Copy to Clipboard
- **Button**: "Copy All (Filtered)"
- **Format**: Tab-separated text
- **Content**: All visible columns and rows
- **Use Case**: Quick sharing or pasting into other applications

### CSV Export
- **Button**: "Export CSV"
- **Format**: Comma-separated values
- **File Extension**: `.csv`
- **Use Case**: Spreadsheet applications, data analysis tools

### Excel Export
- **Button**: "Export Excel"
- **Format**: Microsoft Excel spreadsheet
- **File Extension**: `.xlsx`
- **Use Case**: Professional reports, advanced analysis

### PDF Export
- **Button**: "Export PDF"
- **Format**: Portable Document Format
- **File Extension**: `.pdf`
- **Use Case**: Final reports, presentations, documentation

## Export Behavior

### Filtered Data Only
- **Scope**: Only exports visible/filtered rows
- **Benefits**: Focused reports, relevant data only
- **Example**: Filter by "Red" severity → Export → Only Red items included

### Column Visibility
- **Respects**: Hidden columns are excluded
- **Benefits**: Clean reports, focused content
- **Example**: Hide UNC column → Export → UNC paths not included

### Current View
- **Scope**: Exports exactly what you see
- **Includes**: Applied filters, visible columns, current page
- **Benefits**: Consistent with your analysis view

## Export Workflows

### Basic Export
1. **Load Data**: Upload your Snaffler CSV
2. **Apply Filters**: Use search and column filters
3. **Select Format**: Choose export type
4. **Click Export**: Download the file
5. **Review**: Check exported data

### Review-Based Export
1. **Mark Items**: Use review system to mark items
2. **Filter by Status**: Show only reviewed items
3. **Export**: Create report of reviewed findings
4. **Repeat**: Export pending items separately

### Severity-Based Export
1. **Filter by Severity**: Start with Red items
2. **Export Critical**: Create critical findings report
3. **Continue**: Export Yellow, Green, Black separately
4. **Combine**: Merge reports as needed

### Team Collaboration Export
1. **Initial Export**: Export all data for team
2. **Individual Analysis**: Team members work separately
3. **Progress Export**: Export reviewed items
4. **Final Export**: Export all completed analysis

## Export Features

### Data Formatting
- **Headers**: Column names included
- **Formatting**: Maintains table structure
- **Encoding**: UTF-8 for international characters
- **Compatibility**: Works with standard applications

### File Naming
- **Default**: `lazysnaffler_export_[timestamp]`
- **Format**: Includes date and time
- **Uniqueness**: Prevents file overwrites
- **Customization**: Rename after download

### Export Settings
- **Enable/Disable**: Control which exports are available
- **Settings Panel**: Configure export options
- **Persistence**: Settings saved across sessions
- **Team Sharing**: Export settings with team

## Advanced Export Options

### Custom Column Selection
1. **Hide Columns**: Use "Show/Hide Columns"
2. **Export**: Only visible columns included
3. **Benefits**: Focused reports, reduced file size
4. **Use Case**: Executive summaries, specific analysis

### Filtered Exports
1. **Apply Filters**: Use search and column filters
2. **Export**: Only filtered data included
3. **Benefits**: Targeted reports, relevant content
4. **Use Case**: Specific file types, severity levels

### Multi-Format Exports
1. **CSV**: For data analysis
2. **Excel**: For formatted reports
3. **PDF**: For presentations
4. **Copy**: For quick sharing

## Export Best Practices

### Data Preparation
1. **Clean Data**: Remove unnecessary columns
2. **Apply Filters**: Focus on relevant findings
3. **Review Status**: Mark items as reviewed
4. **Verify Content**: Check data before export

### File Management
1. **Naming**: Use descriptive file names
2. **Organization**: Create folders for different exports
3. **Versioning**: Include dates in file names
4. **Backup**: Keep copies of important exports

### Team Workflows
1. **Standardize**: Agree on export formats
2. **Document**: Explain export contents
3. **Share**: Use consistent naming conventions
4. **Review**: Check exports before sharing

### Quality Control
1. **Verify Data**: Check exported content
2. **Test Formats**: Ensure files open correctly
3. **Validate**: Confirm data integrity
4. **Document**: Note any data limitations

## Troubleshooting

### Export Not Working
- **Check Data**: Ensure data is loaded
- **Verify Filters**: Check filter settings
- **Browser Issues**: Try different browser
- **File Permissions**: Check download permissions

### File Format Issues
- **CSV**: Use text editor to check format
- **Excel**: Verify file isn't corrupted
- **PDF**: Check PDF viewer compatibility
- **Encoding**: Ensure UTF-8 encoding

### Performance Issues
- **Large Data**: Reduce data size before export
- **Memory**: Close other applications
- **Browser**: Use latest browser version
- **Timeout**: Wait for export to complete

### Data Missing
- **Filters**: Check applied filters
- **Columns**: Verify column visibility
- **Page**: Ensure all data is visible
- **Status**: Check review status filters

## Export Reference

### Supported Applications
- **CSV**: Excel, Google Sheets, LibreOffice Calc
- **Excel**: Microsoft Excel, LibreOffice Calc
- **PDF**: Adobe Reader, Chrome, Firefox
- **Copy**: Any text editor, email, chat

### File Size Limits
- **CSV**: No practical limit
- **Excel**: ~1 million rows
- **PDF**: Depends on content complexity
- **Copy**: Browser clipboard limits

### Export Timing
- **Small Data**: < 1 second
- **Medium Data**: 1-5 seconds
- **Large Data**: 5-30 seconds
- **Very Large**: May timeout, reduce data size
