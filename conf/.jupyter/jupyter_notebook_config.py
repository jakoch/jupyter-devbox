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

# for IPython Kernel Options, see https://ipython.readthedocs.io/en/stable/config/options/kernel.html
c.IPKernelApp.pylab = 'inline'        # in-line figure when using Matplotlib

c.ServerApp.ip = '*'                  # Set ip to '*' to bind on all interfaces (ips) for the public server
#c.NotebookApp.ip = '0.0.0.0'
c.ServerApp.port = 8888
c.ServerApp.open_browser = False      # do not open a browser window by default when using notebooks
c.IdentityProvider.token = ''         # No token. Always use jupyter over ssh tunnel (formerly ServerApp.token)
c.LabApp.token = ''                   # No token. Always use jupyter over ssh tunnel
c.ServerApp.password = ''
c.ServerApp.root_dir = "/workspaces/jupyter-devbox/notebooks"
c.ServerApp.allow_root = True         # Allow to run Jupyter from root user inside Docker container
c.ServerApp.allow_origin = '*'
c.ServerApp.allow_remote_access = True
c.ServerApp.tornado_settings = {
    'headers': {
        'Access-Control-Allow-Private-Network': 'true',
        'Content-Security-Policy': "frame-ancestors 'self' *"
    }
}

# this name needs to match the kernel name set by "ipykernel install --name" in the Dockerfile
# you can list all available kernels using `jupyter kernelspec list` on the CLI
# you can check for the "default" kernel via jupyter api endpoint http://localhost:8888/api/kernelspecs
c.MultiKernelManager.default_kernel_name = 'jupyter_devbox'

# to output both image/svg+xml and application/pdf plot formats in the notebook file
c.InlineBackend.figure_formats = {"png", "jpeg", "svg", "pdf"}
