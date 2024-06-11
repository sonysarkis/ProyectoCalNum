using Pkg

packages = [
    "SymPy",
    "Interpolations",
    "Plots",
    "CSV",
    "DataFrames",
    "Statistics",
    "PyCall"
]

for pkg in packages
    Pkg.add(pkg)
end
