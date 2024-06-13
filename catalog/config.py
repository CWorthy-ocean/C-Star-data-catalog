import os

# specify where to keep cached data files
os.environ["INTAKE_LOCAL_CACHE_DIR"] = os.environ["TMPDIR"]