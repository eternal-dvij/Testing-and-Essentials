import re
import os
 
def update_deprecated_finders(file_path):
    try:
 
        with open(file_path, 'r') as a:
            code = a.read()
 
            find_dict = {
                'find_element_by_id(': 'find_element(By.ID',
                'find_element_by_name(': 'find_element(By.NAME,',
                'find_element_by_xpath(': 'find_element(By.XPATH,',
                'find_element_by_link_text(': 'find_element(By.LINK_TEXT,',
                'find_element_by_partial_link_text(': 'find_element(By.PARTIAL_LINK_TEXT,',
                'find_element_by_tag_name(': 'find_element(By.TAG_NAME,',
                'find_element_by_class_name(': 'find_element(By.CLASS_NAME,',
                'find_element_by_css_selector(': 'find_element(By.CSS_SELECTOR,',
                'find_elements_by_id(': 'find_elements(By.ID,',
                'find_elements_by_name(': 'find_elements(By.NAME,',
                'find_elements_by_xpath(': 'find_elements(By.XPATH,',
                'find_elements_by_link_text(': 'find_elements(By.LINK_TEXT,',
                'find_elements_by_partial_link_text(': 'find_elements(By.PARTIAL_LINK_TEXT,',
                'find_elements_by_tag_name(': 'find_elements(By.TAG_NAME,',
                'find_elements_by_class_name(': 'find_elements(By.CLASS_NAME,',
                'find_elements_by_css_selector(': 'find_elements(By.CSS_SELECTOR,'
 
            }
 
            for old_find, new_find in find_dict.items():
                # code = re.sub(f'{old_find}', f'{new_find}', code)
                # code = re.sub(fr'{re.escape(old_find)}\s*\(\s*["\']([^"\']+)["\']\s*\)?', rf'{new_find}, "\1")', f'{code}')
                code = code.replace(old_find,new_find)
        with open(file_path, 'w') as ad:
            ad.write(code)
 
        print(f'update_deprecated_finders() says: updated {file_path}')
 
    except FileNotFoundError as f:
        print(f)
 
    except Exception as e:
        print(f'error: {e}')
 
 
def multifiles():
    folder_path = input("Enter the folder in which you have placed all files: ")
 
    file_ct = os.listdir(folder_path)
 
    for file in file_ct:
        if file.endswith(".py"):
            update_deprecated_finders(f'{folder_path}\\{file}')
            print(f'multifiles() says: updated deprecated finders in {file} ')
        else:
            print(f'skipping {file} since it is not a python file')
 
 
 
 
# <test>
multifiles()
# </test>
