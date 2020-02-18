{ pkgs ? import <nixpkgs> {} }:
pkgs.python3Packages.callPackage ./default.nix {}
