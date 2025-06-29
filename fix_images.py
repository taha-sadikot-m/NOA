import os
import re

def fix_image_references():
    """Fix image references in HTML templates by replacing URL-encoded spaces with actual spaces"""
    
    # Files to fix
    template_files = [
        'templates/index.html',
        'templates/features.html', 
        'templates/pricing.html',
        'templates/about.html',
        'templates/contact.html',
        'templates/404.html',
        'templates/500.html'
    ]
    
    # Image files that need fixing (from the 404 errors)
    image_fixes = {
        '66f2538bc11df4e06933f3a5_WLTH%20Thin.png': '66f2538bc11df4e06933f3a5_WLTH Thin.png',
        '66f2538bc11df4e06933f3a5_WLTH%20Thin-p-500.png': '66f2538bc11df4e06933f3a5_WLTH Thin-p-500.png',
        '66f2538bc11df4e06933f3a5_WLTH%20Thin-p-800.png': '66f2538bc11df4e06933f3a5_WLTH Thin-p-800.png',
        '66f257dcb7e01b8ca88410bc_Top%20Left.svg': '66f257dcb7e01b8ca88410bc_Top Left.svg',
        '66f259b32188a2962beb6d0b_Bottom%20Left.svg': '66f259b32188a2962beb6d0b_Bottom Left.svg',
        '66f25bfadd1d6739297ac960_Bottom%20Right%20.svg': '66f25bfadd1d6739297ac960_Bottom Right .svg',
        '66f25cd00629b62fa3a975c5_Top%20Left%20Long.svg': '66f25cd00629b62fa3a975c5_Top Left Long.svg',
        '66f25dc0a21e0d0875d8d501_Bottom%20Left%20Long.svg': '66f25dc0a21e0d0875d8d501_Bottom Left Long.svg'
    }
    
    for template_file in template_files:
        if os.path.exists(template_file):
            print(f"Processing {template_file}...")
            
            # Read the file
            with open(template_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Apply fixes
            original_content = content
            for old_name, new_name in image_fixes.items():
                content = content.replace(old_name, new_name)
            
            # Write back if changes were made
            if content != original_content:
                with open(template_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  Fixed image references in {template_file}")
            else:
                print(f"  No changes needed in {template_file}")
        else:
            print(f"File not found: {template_file}")

if __name__ == "__main__":
    fix_image_references()
    print("Image reference fixes completed!") 