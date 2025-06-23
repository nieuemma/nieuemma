# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running ‘nixos-help’).

{ config, pkgs, lib, ... }:

{
  imports =
    [ ./hardware-configuration.nix ];

  # Bootloader.
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;
  boot.loader.timeout = 0;
  
  boot.kernelPackages = pkgs.linuxPackages_latest; # Use latest kernel

  networking.hostName = "nixos"; # Define your hostname

  networking.networkmanager.enable = true; # Enable networking

  time.timeZone = "America/New_York"; # Set your time zone

  # Set locales
  i18n.defaultLocale = "de_DE.UTF-8";

  i18n.extraLocaleSettings = {
    LC_ADDRESS = "de_DE.UTF-8";
    LC_IDENTIFICATION = "de_DE.UTF-8";
    LC_MEASUREMENT = "de_DE.UTF-8";
    LC_MONETARY = "de_DE.UTF-8";
    LC_NAME = "de_DE.UTF-8";
    LC_NUMERIC = "de_DE.UTF-8";
    LC_PAPER = "de_DE.UTF-8";
    LC_TELEPHONE = "de_DE.UTF-8";
    LC_TIME = "de_DE.UTF-8";
  };

  # Configure keymap in X11
  services.xserver.xkb = {
    layout = "us";
    variant = "";
  };

  # Define a user account
  users.users.emma = {
    shell = pkgs.nushell;
    isNormalUser = true;
    description = "emma";
    extraGroups = [ "networkmanager" "wheel" ];
    packages = with pkgs; [];
  };

  # Enable automatic login
  services.getty.autologinUser = "emma";
  
  # Enable Hyprland WM
  programs.hyprland = {
    enable = true;
    withUWSM = true;
    xwayland.enable = true;
  };
  
  # List systemwide packages
  environment.systemPackages = with pkgs; [
  anyrun
  atuin
  blender
  bluetui
  bluez
  bottom
  clipse
  cmus
  freetube
  gh
  gimp
  git
  helix
  hypridle
  hyprlock
  hyprnome
  hyprnotify
  hyprpaper
  hyprpicker
  hyprshot
  imv
  jdk
  kitty
  macchina
  mpv
  nushell
  nwg-look
  onlyoffice-desktopeditors
  ouch
  prismlauncher
  qutebrowser
  rustup
  silicon
  starship
  swayosd
  vesktop
  wl-clipboard
  wlsunset
  wlogout
  yazi
  yaziPlugins.ouch
  zoxide
  ];

  # List services that you want to enable:
  services.openssh = {
    enable = true;
    ports = [ 22 ];
    settings = {
      PasswordAuthentication = true;
      AllowUsers = [ "emma" ];
      UseDns = true;
      X11Forwarding = false;
      PermitRootLogin = "prohibit-password";
  };
};

  # Configure the firewall
  networking.firewall.allowedTCPPorts = [ 22 ];
  networking.firewall.allowedUDPPorts = [ 22 ];
  networking.firewall.enable = true;

  system.stateVersion = "25.05";

}
