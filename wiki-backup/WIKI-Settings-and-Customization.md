# Settings and Customization

The LazySnaffler settings panel allows you to customize the dashboard appearance, behavior, and data management options.

## Accessing Settings

1. **Click Settings**: In the sidebar navigation
2. **Settings Modal**: Opens with customization options
3. **Save Changes**: Click "Save Settings" to apply
4. **Auto-Close**: Modal closes automatically after saving

## Appearance Settings

### Theme Selection
- **Light Theme**: Clean, bright interface
- **Dark Theme**: Dark interface for low-light environments
- **Auto-Apply**: Changes apply immediately after saving

### Chart Type
- **Doughnut Chart**: Circular chart with center hole
- **Pie Chart**: Full circular chart
- **Bar Chart**: Horizontal bar representation
- **Auto-Update**: Charts update immediately after saving

## Data Table Settings

### Rows Per Page
- **Options**: 10, 25, 50, 100, All
- **Default**: 25 rows per page
- **Memory**: Setting persists across sessions

### Search Functionality
- **Enable Search**: Toggle global search feature
- **Disable Search**: Hide search input field
- **Performance**: Disabling search can improve performance

### Column Sorting
- **Enable Sorting**: Allow column header clicking
- **Disable Sorting**: Prevent column sorting
- **Use Case**: Disable for read-only analysis

## Export Options

### CSV Export
- **Enable**: Allow CSV export functionality
- **Disable**: Hide CSV export button
- **Format**: Standard comma-separated values

### Excel Export
- **Enable**: Allow Excel export functionality
- **Disable**: Hide Excel export button
- **Format**: Microsoft Excel spreadsheet

### PDF Export
- **Enable**: Allow PDF export functionality
- **Disable**: Hide PDF export button
- **Format**: Portable Document Format

## Data Management

### Clear All Data
- **Function**: Removes all loaded data
- **Scope**: Clears table, charts, and review status
- **Confirmation**: Requires confirmation before clearing
- **Use Case**: Start fresh with new dataset

### Export Settings
- **Format**: JSON file
- **Content**: All current settings
- **Use Case**: Backup or share configuration
- **File Name**: `lazysnaffler_settings.json`

### Import Settings
- **Format**: JSON file
- **Source**: Previously exported settings
- **Validation**: Checks file format before importing
- **Backup**: Current settings are backed up before import

## Settings Persistence

### Browser Storage
- **Location**: localStorage
- **Scope**: Per-browser, per-domain
- **Persistence**: Survives browser restarts
- **Privacy**: Settings stay on your machine

### Default Values
- **Theme**: Light
- **Chart Type**: Doughnut
- **Rows Per Page**: 25
- **Search**: Enabled
- **Sorting**: Enabled
- **Exports**: All enabled

## Advanced Customization

### Theme Customization
- **CSS Variables**: Theme colors are customizable
- **Browser DevTools**: Inspect and modify CSS
- **Persistence**: Custom themes require manual CSS editing

### Chart Customization
- **Colors**: Chart colors follow theme
- **Labels**: Chart labels are automatically generated
- **Interactivity**: Charts are interactive (hover, click)

### Table Customization
- **Column Width**: Auto-adjusts based on content
- **Row Height**: Standard height for readability
- **Font Size**: Follows browser default settings

## Settings Management

### Export Settings Workflow
1. **Configure**: Set desired options
2. **Save**: Click "Save Settings"
3. **Export**: Click "Export Settings"
4. **Download**: Save JSON file
5. **Share**: Send file to team members

### Import Settings Workflow
1. **Prepare**: Have settings JSON file ready
2. **Import**: Click "Import Settings"
3. **Select**: Choose the JSON file
4. **Apply**: Settings are applied immediately
5. **Save**: Click "Save Settings" to persist

### Reset to Defaults
1. **Clear Data**: Use "Clear All Data"
2. **Refresh**: Reload the page
3. **Defaults**: All settings return to default values

## Best Practices

### Theme Selection
- **Light Theme**: Use in well-lit environments
- **Dark Theme**: Use in low-light or extended sessions
- **Consistency**: Stick to one theme for team workflows

### Performance Optimization
- **Disable Search**: For large datasets
- **Reduce Rows**: Use smaller page sizes
- **Disable Sorting**: For read-only analysis

### Team Collaboration
- **Export Settings**: Share configuration files
- **Standardize**: Agree on common settings
- **Document**: Keep settings files in version control

### Data Management
- **Regular Exports**: Export settings periodically
- **Backup**: Keep settings files safe
- **Clear Data**: Start fresh for new projects

## Troubleshooting

### Settings Not Saving
- **Check Storage**: Verify browser localStorage
- **Permissions**: Ensure browser allows storage
- **JavaScript**: Verify JavaScript is enabled

### Import Failed
- **File Format**: Ensure JSON file is valid
- **File Size**: Check file isn't corrupted
- **Permissions**: Verify file is readable

### Performance Issues
- **Reduce Rows**: Use smaller page sizes
- **Disable Features**: Turn off unused options
- **Clear Data**: Remove old data regularly

### Theme Issues
- **Browser Cache**: Clear browser cache
- **CSS Conflicts**: Check for conflicting styles
- **JavaScript Errors**: Check browser console

## Settings Reference

### Default Configuration
```json
{
  "theme": "light",
  "chartType": "doughnut",
  "pageLength": 25,
  "enableSearch": true,
  "enableSorting": true,
  "enableCSV": true,
  "enableExcel": true,
  "enablePDF": true
}
```

### Settings File Location
- **Browser**: localStorage
- **Key**: `lazysnaffler_settings`
- **Format**: JSON string
- **Access**: Browser DevTools → Application → Local Storage
