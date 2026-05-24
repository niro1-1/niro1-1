# Check for outdated packages

import pkg_resources

# Get the list of installed packages
installed_packages = pkg_resources.working_set

# Create a list of outdated packages
outdated_packages = []

# Check for outdated packages
for package in installed_packages:
    try:
        # Get the latest version of the package
        latest_version = pkg_resources.get_distribution(package.project_name).version
        if package.version != latest_version:
            outdated_packages.append((package.project_name, package.version, latest_version))
    except:
        pass

# Print the outdated packages
if outdated_packages:
    print("Outdated packages:")
    for pkg in outdated_packages:
        print(f"{pkg[0]}: {pkg[1]} -> {pkg[2]}")
else:
    print("All packages are up to date.")
