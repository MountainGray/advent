{
  description = "advent nix dependancy hell";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    rust-overlay = {
      url = "github:oxalica/rust-overlay";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  # Flake outputs that other flakes can use
  outputs = { self,  nixpkgs, rust-overlay }:
    let
      # Nixpkgs overlays
      overlays = [
        rust-overlay.overlays.default
        (final: prev: {
          rustToolchain = final.rust-bin.stable.latest.default;
        })
      ];

      # Helpers for producing system-specific outputs
      supportedSystems = [ "x86_64-linux" "aarch64-darwin" "aarch64-linux" ];
      forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f {
        pkgs = import nixpkgs { inherit overlays system; };
      });
    in {
      
      # Development environments
      devShells = forEachSupportedSystem ({ pkgs }: {
        default = pkgs.mkShell {
          # Pinned packages available in the environment
          packages = with pkgs; [
            rustToolchain
            cargo-watch
            rust-analyzer
            jq
            nixpkgs-fmt
            openssl
            pkg-config
            libiconv
          ];

          # Environment variables
          env = {
            RUST_BACKTRACE = "1";
          };

          # A hook run every time you enter the environment
          shellHook = ''
            echo "merry xmas"
          '';
        };
      });
    };
}
