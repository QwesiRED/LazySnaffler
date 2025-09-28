# How to Set Up GitHub Wiki

This guide explains how to add the wiki content to your GitHub repository.

## Step 1: Enable Wiki on GitHub

1. **Go to your repository**: Navigate to your LazySnaffler repository on GitHub
2. **Click "Settings"**: In the repository navigation bar
3. **Scroll to "Features"**: Find the Features section
4. **Enable Wiki**: Check the "Wikis" checkbox
5. **Save**: Click "Save changes"

## Step 2: Access the Wiki

1. **Wiki Tab**: Click the "Wiki" tab in your repository navigation
2. **Create Home Page**: GitHub will prompt you to create the first page
3. **Start Editing**: Click "Create the first page"

## Step 3: Add Wiki Pages

### Home Page (WIKI-Home.md)
1. **Title**: "Home"
2. **Content**: Copy the content from `WIKI-Home.md`
3. **Save**: Click "Save Page"

### Dashboard Overview (WIKI-Dashboard-Overview.md)
1. **New Page**: Click "New Page"
2. **Title**: "Dashboard-Overview"
3. **Content**: Copy the content from `WIKI-Dashboard-Overview.md`
4. **Save**: Click "Save Page"

### Data Table Features (WIKI-Data-Table-Features.md)
1. **New Page**: Click "New Page"
2. **Title**: "Data-Table-Features"
3. **Content**: Copy the content from `WIKI-Data-Table-Features.md`
4. **Save**: Click "Save Page"

### Review System (WIKI-Review-System.md)
1. **New Page**: Click "New Page"
2. **Title**: "Review-System"
3. **Content**: Copy the content from `WIKI-Review-System.md`
4. **Save**: Click "Save Page"

### Settings and Customization (WIKI-Settings-and-Customization.md)
1. **New Page**: Click "New Page"
2. **Title**: "Settings-and-Customization"
3. **Content**: Copy the content from `WIKI-Settings-and-Customization.md`
4. **Save**: Click "Save Page"

### Export Options (WIKI-Export-Options.md)
1. **New Page**: Click "New Page"
2. **Title**: "Export-Options"
3. **Content**: Copy the content from `WIKI-Export-Options.md`
4. **Save**: Click "Save Page"

### FAQ (WIKI-FAQ.md)
1. **New Page**: Click "New Page"
2. **Title**: "FAQ"
3. **Content**: Copy the content from `WIKI-FAQ.md`
4. **Save**: Click "Save Page"

## Step 4: Organize Wiki Pages

### Create Sidebar
1. **Edit Home Page**: Click "Edit" on the Home page
2. **Add Sidebar**: Add the navigation structure
3. **Save**: Click "Save Page"

### Link Pages
- Use `[Page Name](Page-Name)` format for internal links
- Use `[External Link](https://example.com)` for external links
- Use `[../README.md](../README.md)` for repository files

## Step 5: Customize Wiki

### Add Images
1. **Upload Images**: Use the "Attach files" button
2. **Reference Images**: Use `![Alt text](image-name.png)` format
3. **Organize**: Create folders for different image types

### Add Code Blocks
```markdown
```python
# Python code example
python lazysnaffler.py -f ExampleData/snafflerlog.txt --http
```
```

### Add Tables
```markdown
| Feature | Description | Status |
|---------|-------------|--------|
| Search | Global search | ✅ |
| Filters | Column filters | ✅ |
| Export | Multiple formats | ✅ |
```

## Step 6: Maintain Wiki

### Regular Updates
- Update content when features change
- Add new pages for new features
- Keep links current and working

### Version Control
- Wiki pages are version controlled by GitHub
- View page history for changes
- Revert to previous versions if needed

### Collaboration
- Allow community contributions
- Review changes before accepting
- Maintain consistent formatting

## Alternative: Use GitHub Pages

If you prefer a more advanced documentation site:

1. **Create docs folder**: Add a `docs/` folder to your repository
2. **Add markdown files**: Place wiki content in markdown files
3. **Enable GitHub Pages**: In repository settings
4. **Choose source**: Select "docs folder"
5. **Access site**: Available at `https://username.github.io/repository-name`

## Tips for Success

### Content Organization
- Use clear, descriptive page titles
- Create logical navigation structure
- Keep content focused and concise
- Use consistent formatting

### User Experience
- Add screenshots for complex features
- Include step-by-step instructions
- Provide examples and use cases
- Link related pages

### Maintenance
- Regular content reviews
- Update outdated information
- Monitor for broken links
- Gather user feedback

## Wiki Structure Summary

```
Home
├── Dashboard-Overview
├── Data-Table-Features
├── Review-System
├── Settings-and-Customization
├── Export-Options
└── FAQ
```

This structure provides comprehensive documentation while keeping the main README focused on the Python script functionality.
