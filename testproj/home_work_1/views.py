from django.shortcuts import render

import logging

from django.http import HttpResponse

# from django.shortcuts import render


logger = logging.getLogger('my_logger')

headers = {'Cache-Control': 'no-cache, must-revalidate', 'Pragma': 'no-cache'}

def main(request):
    body = """
    <title>Main page</title>
    <body>
        <div>
            <h1>Main page</h1>
            <p>Content of main page</p>
            <p>Go to page: /about</p>
        </div>
        <footer>
            <div>
                <p>Copyright &copy;
                    <script type="text/javascript"> document.write(new Date().getFullYear());</script>
                    
                </p>
            </div>
        </footer>
    </body>
    """
    logger.info(f'page open: main')
    return HttpResponse(body, charset="utf-8", headers=headers)


def about(request):
    body = """
        <title>About myself</title>  
        <body>     
            <div>
                <h1>Cherepanov Evgeniy Aleksandrovich</h1>
                <p>Male, 38 years old, was born 24 of october 1984</p>
                <p>Go to page: /main</p>
            </div>
            <footer>
                <div>
                    <p>Copyright &copy;
                        <script type="text/javascript"> document.write(new Date().getFullYear());</script>
                        
                    </p>
                </div>
            </footer>
        </body>
        """
    logger.info(f'page open: about')
    return HttpResponse(body, charset="utf-8", headers=headers)