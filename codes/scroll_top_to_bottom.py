# your general imports goes here....

def scroll_top_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, 0);")
    print(f'scrolling started... {time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime())}')
 
    def is_bottom():
        driver.execute_script("""window.isReachedBottom = function() {
                                    return (window.innerHeight +window.scrollY) >= document.body.offsetHeight;
                                    }""")
        is_reached_bottom = driver.execute_script("return window.isReachedBottom();")
        return is_reached_bottom
    timeout = 40
    driver.execute_script("""
                        function smoothScroll() {
                            var totalHeight = 0;
                            var scrollHeight = document.body.scrollHeight;
 
                            function scrollToBottom() {
                                window.scrollTo(0, totalHeight);
                                totalHeight += 2; 
 
                                var newScrollHeight = document.body.scrollHeight;
                                if (newScrollHeight >= scrollHeight) {
                                    scrollHeight = newScrollHeight;
                                    requestAnimationFrame(scrollToBottom);
                                } else {
                                    console.log("Reached bottom!");
                                }
                            }      
                            scrollToBottom();
                        }
 
                        smoothScroll();
                """)
    start_time = time.time()
    for i in range(1,timeout):
        if not is_bottom():
            if time.time() - start_time >timeout:
                break
            else:
                time.sleep(1)
        else:
            break
    # wait not to check frequently to avoid load
    print(f'scrolling ended... {time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime())}')

# <test>
from selenium import webdriver
import time

# Assuming you have a WebDriver executable in the current directory
driver = webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get("https://example.com")
scroll_top_to_bottom(self.driver)
# </test>
