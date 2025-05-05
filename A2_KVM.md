# Assignment A2: KVM Virtualisation

### Step 1: Check for Virtualisation

1. Run the following command to check for virtualisation:
   ```bash
   sudo dmesg | grep kvm
   ```
2. Enter your password if prompted.

3. If there is no output, it indicates virtualisation is enabled.

### Step 2: Downloading VirtualBox Manager

1. Follow all steps mentioned in the handout or use the KSKA Steps.

2. Install the necessary packages 

```bash
sudo apt update
sudo apt install qemu-kvm libvirt-daemon-system virt-manager
```

3. Add current user to the libvirt group 
```bash
sudo adduser $USER libvirt 
```
4. Enable and start the libvirt service 
```bash
sudo systemctl enable libvirtd.service --now
```

5. Log out of the desktop session and relogin (RESART PC). 

6. Open the Virtual Machine Manager app from the application tray, an option titled          
“QEMU/KVM” should appear.


**7. NOTE : If there are errors during installation, fix the missing dependencies by running:**

```bash
sudo apt-get update
sudo apt-get install --fix-missing
```
3. Once missing dependencies are fixed, redo Step 2 from the handout.

### Step 3: Install ISO File for OS
Download Fedora ISO (Workstation) for Intel and AMD x86_64 systems:

[Fedora Workstation Download](https://fedoraproject.org/workstation/download)

OR

[Download Windows 10 ISO](https://www.microsoft.com/en-us/software-download/windows10ISO )

Make sure to download the English (x64 bit) version.

### STEP 4: Create new VM
1.	Open virtual machine from apps
2.	Click on “Create new Virtual machine”
3.	Choose Local insll media (by default) Click forward
4.	Select your iso file and click on forward
5.	Choose memory and CPU (recommended : Memory : 4096 CPU: 4) Click forward
6.	Select 50gb as disk space Click forward
7.	Enter any name for your Virtaul Machine and click finish
8.	Complete the setup
