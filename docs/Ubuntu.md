# Ubuntu Notes


## Periodic Update

### Update Package Lists:
   Refresh the list of available packages and their versions with the command:
   `sudo apt update`

### Upgrade Installed Packages:
   Upgrade all installed packages to their latest versions using:
   `sudo apt upgrade`

## Optional - Dist-Upgrade:
   For a more intelligent handling of dependencies and to upgrade to new versions of packages, use:
   `sudo apt dist-upgrade`
   This command may remove some packages if necessary.

### Clean Up:
   After upgrading, remove packages that are no longer needed to manage disk space:
   sudo apt autoremove

### Check System Reboot Requirement:
   After some updates, especially kernel updates, a reboot might be required. Check this with:
   `[ -f /var/run/reboot-required ] && echo 'Reboot required'`
