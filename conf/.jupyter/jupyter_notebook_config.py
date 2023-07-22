#
# Jupyter Notebook Config
#
# https://jupyter-notebook.readthedocs.io/en/master/config.html
#
c = get_config()  # get the config object
c.IPKernelApp.pylab = 'inline'  # in-line figure when using Matplotlib
#c.NotebookApp.ip = '*' # Set ip to '*' to bind on all interfaces (ips) for the public server
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False  # do not open a browser window by default when using notebooks
c.NotebookApp.token = '' # No token. Always use jupyter over ssh tunnel
c.LabApp.token = '' # No token. Always use jupyter over ssh tunnel
c.NotebookApp.password = ''
c.NotebookApp.notebook_dir = "/workspaces/jupyter-devbox/notebooks"
c.NotebookApp.allow_root = True # Allow to run Jupyter from root user inside Docker container
c.NotebookApp.allow_origin = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' *"
    }
}
# to output both image/svg+xml and application/pdf plot formats in the notebook file
c.InlineBackend.figure_formats = {"png", "jpeg", "svg", "pdf"}
