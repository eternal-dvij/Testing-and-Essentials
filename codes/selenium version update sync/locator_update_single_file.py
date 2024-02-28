import re
import os
 
def update_deprecated_finders_single_file():
  file_path = input("Enter the file path you want to update : ") 
  # example: C://Users/xyz//Downloads//test_script.py
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
                code = code.replace(old_find,new_find)
        with open(file_path, 'w') as ad:
            ad.write(code)
 
        print(f'update_deprecated_finders() says: updated {file_path}')
 
    except FileNotFoundError as f:
        print(f)
 
    except Exception as e:
        print(f'error: {e}')
 

 
 
 
# <test>
update_deprecated_finders_single_file()
# </test>
