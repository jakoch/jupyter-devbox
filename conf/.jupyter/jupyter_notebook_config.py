#
# Jupyter Notebook Config
#
# https://jupyter-notebook.readthedocs.io/en/master/config.html
#
#
# To generate a config with all defaults commented out use:
# > jupyter notebook --generate-config
#

c = get_config()  # noqa - get the config object

# for IPython Kernel Options, see https://ipython.readthedocs.io/en/stable/config/options/kernel.html
c.IPKernelApp.pylab = "inline"  # in-line figure when using Matplotlib

# Set ip to '*' to bind on all interfaces (ips) for the public server
c.ServerApp.ip = "*"
# c.NotebookApp.ip = '0.0.0.0'
c.ServerApp.port = 8888
# do not open a browser window by default when using notebooks
c.ServerApp.open_browser = False
# No token. Always use jupyter over ssh tunnel (formerly ServerApp.token)
c.IdentityProvider.token = ""
# No token. Always use jupyter over ssh tunnel
c.LabApp.token = ""
c.ServerApp.password = ""
c.ServerApp.root_dir = "/workspaces/jupyter-devbox/notebooks"
# Allow to run Jupyter from root user inside Docker container
c.ServerApp.allow_root = True
c.ServerApp.allow_origin = "*"
c.ServerApp.allow_remote_access = True
c.ServerApp.tornado_settings = {
    "headers": {
        "Access-Control-Allow-Private-Network": "true",
        "Content-Security-Policy": "frame-ancestors 'self' *",
    }
}
# this name needs to match the kernel name set by "ipykernel install --name" in the Dockerfile
# you can list all available kernels using `jupyter kernelspec list` on the CLI
# you can check for the "default" kernel via jupyter api endpoint http://localhost:8888/api/kernelspecs
c.MultiKernelManager.default_kernel_name = "jupyter_devbox"

# to output both image/svg+xml and application/pdf plot formats in the notebook file
c.InlineBackend.figure_formats = {"png", "jpeg", "svg", "pdf"}

# JupyterLab Code Formatter settings
# Note:
# "black --skip-errors" is added to allow the python code blocks to
# include jupyter-specific magic commands starting with % or !
# Both chars result in a syntax error when black tries to format the code cell.
c.JupyterLabCodeFormatter.formatters = {
    "black": {
        "module": "jupyterlab_code_formatter.formatters.black",
        "args": ["--line-length=80", "--skip-magic-trailing-comma"],
    },
    "isort": {
        "module": "jupyterlab_code_formatter.formatters.isort",
        "args": ["--profile=black"],
    },
}
c.JupyterLabCodeFormatter.default_formatter = "black"
c.JupyterLabCodeFormatter.format_on_save = True

# Configure python-lsp-server for JupyterLab LSP extension
c.LanguageServerManager.language_servers = {
    "pylsp": {
        "argv": ["pylsp"],
        "languages": ["python"],
        "version": 2,
        "serverSettings": {
            "pylsp.plugins.black.enabled": true,
            "pylsp.plugins.isort.enabled": true,
            "pylsp.plugins.ruff.enabled": true,
        },
    }
}
