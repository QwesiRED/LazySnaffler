# Data Table Features

The LazySnaffler data table is the core of the dashboard, providing powerful tools for analyzing Snaffler findings.

## Table Structure

### Columns
- **Actions**: Review checkboxes and "View Full" buttons
- **Severity**: Red, Yellow, Green, Black classifications
- **Rule**: Snaffler rule that triggered the finding
- **Keyword**: Specific keyword or pattern matched
- **Modified**: File modification timestamp
- **Extension**: File extension (.dll, .txt, etc.)
- **UNC**: Network path to the file
- **Content**: File content snippet
- **Status**: Review status (Reviewed/Pending)

## Search and Filtering

### Global Search
- **Location**: Top of the table
- **Function**: Searches across all columns simultaneously
- **Usage**: Type any term to find matching rows
- **Examples**: 
  - "password" - finds all rows containing "password"
  - "dll" - finds all .dll files
  - "2025-07-17" - finds files modified on that date

### Column-Specific Filters
- **Severity Filter**: Dropdown with Red, Yellow, Green, Black options
- **Rule Filter**: Dynamic dropdown populated with unique rules
- **Extension Filter**: Dynamic dropdown with file extensions
- **Status Filter**: Reviewed/Pending options

### Filter Combinations
- Use global search for broad discovery
- Apply column filters for precise results
- Combine multiple filters for targeted analysis
- Clear all filters with "Clear Filters" button

## Column Management

### Show/Hide Columns
- **Button**: "Show/Hide Columns" in the action bar
- **Function**: Toggle column visibility
- **Use Cases**: 
  - Hide UNC paths for cleaner view
  - Focus on specific data types
  - Customize table for different analysis needs

### Column Sorting
- **Method**: Click column headers
- **Indicators**: Arrow icons show sort direction
- **Multi-sort**: Hold Shift while clicking headers
- **Default**: Severity (ascending), then Modified (descending)

## Review System

### Mark as Reviewed
- **Location**: Actions column
- **Method**: Click the checkbox icon
- **Visual Feedback**: 
  - ✅ Green checkmark = Reviewed
  - ⬜ Gray box = Pending
- **Persistence**: Status saved across sessions

### Status Filtering
- **Filter Options**: All, Reviewed, Pending
- **Location**: Status column filter dropdown
- **Workflow**: Mark items → Filter by status → Export results

## Export Options

### Available Formats
- **Copy**: Copy filtered data to clipboard
- **CSV**: Export as comma-separated values
- **Excel**: Export as Excel spreadsheet
- **PDF**: Export as PDF document

### Export Behavior
- **Filtered Data**: Only exports visible/filtered rows
- **Column Selection**: Respects column visibility settings
- **Formatting**: Maintains table formatting in exports

## Advanced Features

### Row Details
- **"View Full" Button**: Opens detailed modal
- **Content**: Shows complete file content
- **Copy Function**: Copy all details to clipboard
- **Navigation**: Close with X or click outside

### Real-time Updates
- **Filter Changes**: Table updates immediately
- **Review Status**: Visual updates without page refresh
- **Search Results**: Live filtering as you type

## Best Practices

### Efficient Analysis
1. Start with global search for broad discovery
2. Use column filters to narrow results
3. Hide unnecessary columns for focus
4. Mark items as reviewed during analysis
5. Export filtered results for reporting

### Workflow Optimization
- Use keyboard shortcuts for faster navigation
- Combine filters for precise targeting
- Export at different stages of analysis
- Use review status to track progress

## Troubleshooting

### Common Issues
- **Slow Performance**: Reduce visible columns or data size
- **Filter Not Working**: Check for typos or case sensitivity
- **Export Problems**: Ensure data is loaded and filtered correctly
- **Review Status Lost**: Check browser localStorage settings

### Performance Tips
- Hide unused columns
- Use specific filters instead of broad searches
- Clear filters when switching analysis focus
- Export data periodically to avoid data loss
