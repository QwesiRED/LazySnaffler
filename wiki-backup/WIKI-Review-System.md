# Review System

The LazySnaffler review system helps you track which findings have been analyzed and which still need attention.

## Overview

The review system allows you to:
- Mark findings as reviewed or pending
- Filter by review status
- Track analysis progress
- Export reviewed/pending items separately
- Maintain review status across sessions

## How to Use

### Marking Items as Reviewed

1. **Locate the Item**: Find the finding in the data table
2. **Click the Checkbox**: In the Actions column, click the checkbox icon
3. **Visual Confirmation**: 
   - ✅ Green checkmark = Reviewed
   - ⬜ Gray box = Pending
4. **Status Update**: The Status column updates immediately

### Marking Items as Pending

1. **Click Reviewed Item**: Click the green checkmark
2. **Status Change**: Item changes back to pending
3. **Visual Update**: Checkbox returns to gray box

## Status Column

### Status Badges
- **Reviewed**: Green badge with checkmark icon
- **Pending**: Yellow badge with clock icon

### Status Filter
- **Location**: Below the Status column header
- **Options**: All, Reviewed, Pending
- **Function**: Filter table to show only selected status

## Workflow Examples

### Basic Review Workflow
1. **Load Data**: Upload your Snaffler CSV
2. **Initial Filter**: Use global search or column filters
3. **Review Items**: Click checkboxes to mark as reviewed
4. **Track Progress**: Use Status filter to see remaining items
5. **Export Results**: Export reviewed items for reporting

### Advanced Review Workflow
1. **Severity Focus**: Filter by Red severity items first
2. **Review Critical**: Mark high-priority items as reviewed
3. **Export Critical**: Export reviewed critical items
4. **Continue Analysis**: Filter by Yellow severity
5. **Complete Review**: Work through all severity levels

### Team Review Workflow
1. **Initial Pass**: One team member reviews all items
2. **Export Pending**: Export items marked as pending
3. **Second Review**: Another team member reviews pending items
4. **Final Export**: Export all reviewed items for final report

## Filtering by Review Status

### Show Only Reviewed Items
1. Click Status filter dropdown
2. Select "Reviewed"
3. Table shows only reviewed items
4. Export if needed

### Show Only Pending Items
1. Click Status filter dropdown
2. Select "Pending"
3. Table shows only pending items
4. Continue review process

### Show All Items
1. Click Status filter dropdown
2. Select "All"
3. Table shows all items regardless of status

## Exporting by Review Status

### Export Reviewed Items
1. Filter by "Reviewed" status
2. Click desired export button (CSV, Excel, PDF)
3. Only reviewed items are exported

### Export Pending Items
1. Filter by "Pending" status
2. Click desired export button
3. Only pending items are exported

### Export All Items
1. Ensure Status filter is set to "All"
2. Click export button
3. All items are exported with their review status

## Persistence

### Session Persistence
- Review status is saved automatically
- Status persists when switching between Dashboard and Table views
- Status remains when applying filters

### Browser Storage
- Review status is stored in browser localStorage
- Data persists across browser sessions
- Clearing browser data will reset review status

### Data Reload
- Review status is cleared when new data is loaded
- This prevents confusion with different datasets
- Export review status before loading new data if needed

## Best Practices

### Review Strategy
1. **Start with High Severity**: Review Red items first
2. **Use Filters**: Focus on specific file types or rules
3. **Batch Review**: Review similar items together
4. **Regular Exports**: Export progress periodically

### Status Management
1. **Clear Status**: Use "Clear All Data" to reset review status
2. **Export Before Clear**: Save review status before clearing
3. **Team Coordination**: Agree on review standards
4. **Documentation**: Use exports to document review progress

### Workflow Optimization
1. **Keyboard Navigation**: Use Tab to navigate between items
2. **Bulk Operations**: Use filters to focus on specific groups
3. **Progress Tracking**: Use Status filter to monitor progress
4. **Quality Control**: Periodically review marked items

## Troubleshooting

### Review Status Not Saving
- Check browser localStorage settings
- Ensure JavaScript is enabled
- Try refreshing the page

### Status Filter Not Working
- Verify filter dropdown is set correctly
- Check for conflicting filters
- Clear all filters and try again

### Lost Review Status
- Check if new data was loaded
- Verify browser storage settings
- Export review status before major changes

### Performance Issues
- Limit visible columns during review
- Use filters to reduce table size
- Clear review status if table becomes too large
