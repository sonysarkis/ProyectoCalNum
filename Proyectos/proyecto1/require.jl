using Pkg

packages = [
    "SymPy",
    "Interpolations",
    "Plots",
    "CSV",
    "DataFrames",
    "Statistics"
]

for pkg in packages
    Pkg.add(pkg)
end
