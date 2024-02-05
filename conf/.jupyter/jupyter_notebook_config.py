#
# Jupyter Notebook Config
#
# https://jupyter-notebook.readthedocs.io/en/master/config.html
#
#
# To generate a config with all defaults commented out use:
# > jupyter notebook --generate-config
#

c = get_config() # noqa - get the config object

c.IPKernelApp.pylab = 'inline'        # in-line figure when using Matplotlib
c.ServerApp.ip = '*'                  # Set ip to '*' to bind on all interfaces (ips) for the public server
#c.NotebookApp.ip = '0.0.0.0'
c.ServerApp.port = 8888
c.ServerApp.open_browser = False      # do not open a browser window by default when using notebooks
c.ServerApp.token = ''                # No token. Always use jupyter over ssh tunnel
c.LabApp.token = ''                   # No token. Always use jupyter over ssh tunnel
c.ServerApp.password = ''
c.ServerApp.notebook_dir = "/workspaces/jupyter-devbox/notebooks"
c.ServerApp.allow_root = True # Allow to run Jupyter from root user inside Docker container
c.ServerApp.allow_origin = '*'
c.ServerApp.allow_remote_access = True
c.ServerApp.tornado_settings = {
    'headers': {
        'Access-Control-Allow-Private-Network': 'true',
        'Content-Security-Policy': "frame-ancestors 'self' *"
    }
}

c.MultiKernelManager.default_kernel_name = 'python3'

# to output both image/svg+xml and application/pdf plot formats in the notebook file
c.InlineBackend.figure_formats = {"png", "jpeg", "svg", "pdf"}
