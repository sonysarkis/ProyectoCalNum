using Pkg

function check_and_add(package_name::String)
    if !(package_name in keys(Pkg.installed()))
        Pkg.add(package_name)
    end
end

packages = [
    "SymPy",
    "Interpolations",
    "Plots",
    "CSV",
    "DataFrames",
    "Statistics"
]

for pkg in packages
    check_and_add(pkg)
end
