#!/usr/bin/env python3
"""
GhostLock Ransomware Simulator - Simplified Version
--------------------------------------------
This tool simulates ransomware behavior in a safe, controlled manner.
It is designed for security professionals to test defenses and demonstrate
ransomware behavior without causing actual harm.

By koreyhacks_
"""

import os
import time
import random
import string
import argparse
import logging
import sys
from datetime import datetime

class GhostLockSimulator:
    def __init__(self, target_dir, safe_mode=True, extensions=None, log_file=None):
        """
        Initialize the ransomware simulator.
        
        Args:
            target_dir (str): The target directory to simulate ransomware on
            safe_mode (bool): If True, no actual file operations will be performed
            extensions (list): List of file extensions to target (e.g., ['.txt', '.docx'])
            log_file (str): Path to log file
        """
        self.target_dir = os.path.abspath(target_dir)
        self.safe_mode = safe_mode
        self.extensions = extensions or ['.txt', '.docx', '.xlsx', '.pdf', '.jpg', '.png']
        self.affected_files = []
        self.simulated_key = self._generate_key()
        self.simulation_id = self._generate_simulation_id()
        
        # Setup logging
        self.logger = self._setup_logging(log_file)
    
    def _generate_key(self):
        """Generate a random encryption key (for simulation purposes)"""
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
    
    def _generate_simulation_id(self):
        """Generate a unique simulation ID"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_component = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        return f"GHOST-{timestamp}-{random_component}"
        
    def _setup_logging(self, log_file):
        """Setup logging for the simulator"""
        logger = logging.getLogger('ghostlock_simulator')
        logger.setLevel(logging.INFO)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        
        # File handler if specified
        if log_file:
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.INFO)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            
        return logger
    
    def scan_for_files(self):
        """Scan for files matching the target extensions"""
        self.logger.info(f"Scanning for files in {self.target_dir}...")
        
        # Ghost animation for scanning process
        print("\nGhostLock scanning for files...\n")
        boo_frames = ["(>_>)", "(<_<)", "(^_^)", "(v_v)"]
        frame_idx = 0
        
        file_count = 0
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                # Update animation
                if file_count % 3 == 0:  # Update animation every 3 files
                    frame = boo_frames[frame_idx % len(boo_frames)]
                    sys.stdout.write(f"\r{frame} Scanning... {file_count} files found")
                    sys.stdout.flush()
                    frame_idx += 1
                
                _, ext = os.path.splitext(file)
                if ext.lower() in self.extensions:
                    file_path = os.path.join(root, file)
                    self.affected_files.append(file_path)
                    file_count += 1
        
        # Clear the animation line
        sys.stdout.write("\r" + " " * 50 + "\r")
        sys.stdout.flush()
        
        self.logger.info(f"Scan complete. Found {len(self.affected_files)} files to simulate encryption on.")
        return len(self.affected_files)
    
    def simulate_encryption(self):
        """
        Simulate encryption of files.
        In safe mode, this only logs what would happen.
        In simulation mode, it creates an additional file with .encrypted extension.
        """
        if not self.affected_files:
            self.logger.info("No files to encrypt. Run scan_for_files() first.")
            return
            
        self.logger.info(f"Starting simulated encryption process on {len(self.affected_files)} files...")
        self.logger.info(f"Using simulation key: {self.simulated_key}")
        
        # Ghost animation for encryption process
        print("\nGhostLock encryption in progress...\n")
        boo_frames = ["(>_<)", "(x_x)", "(o_o)", "(0_0)"]
        
        encrypted_count = 0
        for i, file_path in enumerate(self.affected_files):
            # Show animation frame
            if i % 5 == 0:  # Update animation every 5 files
                frame = boo_frames[i % len(boo_frames)]
                sys.stdout.write(f"\r{frame} Encrypting files... {i}/{len(self.affected_files)}")
                sys.stdout.flush()
            if self.safe_mode:
                # In safe mode, just log what would happen
                self.logger.info(f"Would encrypt: {file_path}")
                encrypted_count += 1
                
                # Simulate processing time to make it more realistic
                time.sleep(0.05)
            else:
                # In simulation mode, create a .encrypted marker file
                try:
                    # Create a small marker file to simulate encryption
                    marker_path = f"{file_path}.encrypted.sim"
                    with open(marker_path, 'w') as f:
                        f.write(f"SIMULATION ONLY: This file represents {file_path} encrypted with key {self.simulated_key}\n")
                        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
                        f.write("This is a simulation for educational purposes only.\n")
                    
                    self.logger.info(f"Simulated encryption: {file_path} -> {marker_path}")
                    encrypted_count += 1
                    
                    # Simulate processing time
                    time.sleep(0.1)
                except Exception as e:
                    self.logger.error(f"Error processing {file_path}: {str(e)}")
        
        # Clear the animation line
        sys.stdout.write("\r" + " " * 50 + "\r")
        sys.stdout.flush()
        
        self.logger.info(f"Encryption simulation complete. Affected {encrypted_count} files.")
        return encrypted_count
    
    def display_ransom_note(self):
        """Display a simulated ransom note with animated ghosts"""
        # Ghost appearing animation
        ghost_frames = [
            "    ",
            " .  ",
            " .. ",
            " ...",
            " ...",
            " ..-",
            " .-.",
            " .-.",
            " .-.",
        ]
        
        ghost_eyes = [
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            " o o ",
            "( o o)",
        ]
        
        ghost_body = [
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "|   O",
        ]
        
        ghost_bottom = [
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "'~~~'",
        ]
        
        # Animate the ghost appearing
        for i in range(len(ghost_frames)):
            # Clear screen for each frame
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print(f"\n\n   {ghost_frames[i]}")
            print(f"  {ghost_eyes[i]}")
            print(f"  {ghost_body[i]}")
            print(f"  {ghost_bottom[i]}")
            
            time.sleep(0.2)
        
        # Show final ghost with message
        os.system('cls' if os.name == 'nt' else 'clear')
        note = f"""
{'='*80}
                       GHOSTLOCK RANSOMWARE SIMULATION
{'='*80}

       .--.                   .-.                 .-.           
      : .--'                  : :                 : :           
      : :    .--.  .--.  .--. : :   .--.  .--.   : :   .--.  .--.  .--. 
      : :__ ' .; :' .; :' '_.': :_ ' .; :' .; :  : :_ '  ..'' .; :' '_.'
      `.__.'`.__.'`.___;`.__.':___.'`.__.'`._. ; `.__;`.__.':_.`.'`.__.'
                                           .-. :              
                                           `._.'              

   .-.         .-.         .-.
  ( o o)      ( o o)      ( o o)
  |   O        |   O       |   O
  '~~~'        '~~~'       '~~~'

THIS IS A SIMULATION - NO ACTUAL FILES HAVE BEEN ENCRYPTED

In a real ransomware attack:
- {len(self.affected_files)} files would have been encrypted
- The encryption key would be: {self.simulated_key[:8]}...
- A payment in cryptocurrency would be demanded

This simulation has been run for educational and testing purposes only.

-- Simulation completed by koreyhacks_ --

Timestamp: {datetime.now().isoformat()}
GhostLock Simulation ID: {self.simulation_id}

{'='*80}
"""
        print(note)
        
        # Also save to a file in the target directory
        try:
            with open(os.path.join(self.target_dir, "SIMULATION_RANSOM_NOTE.txt"), 'w') as f:
                f.write(note)
            self.logger.info(f"Ransom note saved to {os.path.join(self.target_dir, 'SIMULATION_RANSOM_NOTE.txt')}")
        except Exception as e:
            self.logger.error(f"Error saving ransom note: {str(e)}")
    
    def cleanup(self):
        """Clean up simulation artifacts"""
        if self.safe_mode:
            self.logger.info("Safe mode enabled, no cleanup needed")
            return
            
        cleaned = 0
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                if file.endswith('.encrypted.sim') or file == "SIMULATION_RANSOM_NOTE.txt":
                    try:
                        os.remove(os.path.join(root, file))
                        cleaned += 1
                    except Exception as e:
                        self.logger.error(f"Error removing {file}: {str(e)}")
        
        self.logger.info(f"Cleanup complete. Removed {cleaned} simulation artifacts.")
        return cleaned


def animate_ghosts():
    """Display an animation of Mario-style ghosts (Boos) moving across the screen"""
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Define ghost (Boo) frames
    ghost1 = [
        "   .-.   ",
        "  ( o o)  ",
        "  |   O   ",
        "  '~~~'   "
    ]
    
    ghost2 = [
        "     .-.   ",
        "    ( o o)  ",
        "    |   O   ",
        "    '~~~'   "
    ]
    
    ghost_shy = [
        "   .-.   ",
        "  ( - -)  ",
        "  |   O   ",
        "  '~~~'   "
    ]
    
    # Terminal width
    width = 80
    
    # Animation
    for i in range(width - 10):
        # Clear screen for each frame
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Print first ghost
        for line in ghost1:
            spaces = " " * i
            print(spaces + line)
        
        # Print second ghost (if appropriate)
        if i > 10:
            for j, line in enumerate(ghost2):
                spaces = " " * (i - 15)
                print(spaces + line)
        
        # Print third ghost (shy one, covering face)
        if i > 25:
            for j, line in enumerate(ghost_shy):
                spaces = " " * (i - 30)
                print(spaces + line)
                
        # Slow down animation
        time.sleep(0.1)
    
    # Final frame - all ghosts disappear
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n\n")
    time.sleep(0.5)


def display_ghostlock_banner():
    """Display the GhostLock ASCII art banner"""
    banner = r"""
  ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓ ██▓     ▒█████   ▄████▄   ██ ▄█▀
 ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒ 
▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░ 
░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ ▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ 
░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄
 ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    ░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░
░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░        ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░ 
      ░  ░  ░  ░    ░ ░        ░               ░  ░    ░ ░  ░ ░      ░  ░   
                                                          ░                  
    By koreyhacks_                                                  v1.0.0

    [*] Advanced Ransomware Simulator For Security Research
    [*] Educational Purposes Only - No Real Encryption Performed
    """
    print(banner)


def main():
    """Main function to run the simulator from command line"""
    parser = argparse.ArgumentParser(description='GhostLock Ransomware Simulator for Educational Purposes')
    parser.add_argument('--target-dir', required=True, help='Target directory for simulation')
    parser.add_argument('--safe-mode', action='store_true', default=True, 
                        help='Run in safe mode (no file operations, default: True)')
    parser.add_argument('--simulate', action='store_false', dest='safe_mode',
                        help='Run simulation (creates marker files, but does not modify original files)')
    parser.add_argument('--extensions', nargs='+', default=['.txt', '.docx', '.xlsx', '.pdf', '.jpg', '.png'],
                        help='File extensions to target')
    parser.add_argument('--log-file', help='Log file path')
    parser.add_argument('--cleanup', action='store_true', help='Clean up simulation artifacts')
    
    args = parser.parse_args()
    
    # Display ghost animation
    animate_ghosts()
    
    # Display the GhostLock banner
    display_ghostlock_banner()
    
    # Confirm user is aware this is a simulation
    print("\n[!] IMPORTANT NOTICE:")
    print("    This is a simulation tool. No actual files will be permanently modified.")
    print(f"    Target directory: {os.path.abspath(args.target_dir)}")
    print(f"    Mode: {'Safe mode (logging only)' if args.safe_mode else 'Simulation mode (creates marker files)'}")
    print()
    
    consent = input("[?] Do you understand this is a simulation and wish to proceed? (yes/no): ")
    if consent.lower() not in ['yes', 'y']:
        print("Simulation aborted.")
        return
    
    try:
        # Create simulator
        simulator = GhostLockSimulator(
            args.target_dir,
            safe_mode=args.safe_mode,
            extensions=args.extensions,
            log_file=args.log_file
        )
        
        if args.cleanup:
            print("Cleaning up previous simulation artifacts...")
            simulator.cleanup()
            return
            
        # Run simulation
        print("\nStarting simulation...")
        simulator.scan_for_files()
        
        print("\nSimulating encryption process...")
        simulator.simulate_encryption()
        
        print("\nSimulation complete.\n")
        simulator.display_ransom_note()
        
        # Offer cleanup
        if not args.safe_mode:
            cleanup = input("\nDo you want to clean up simulation artifacts? (yes/no): ")
            if cleanup.lower() in ['yes', 'y']:
                simulator.cleanup()
    
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        print("Simulation aborted.")


if __name__ == "__main__":
    main()
