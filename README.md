# duplicate_ckl
Duplicate CKL files according to a CSV list of machines.

For situations wherein one checklist is completed and is representative of many other systems, but individual .ckl files
must be created anyways. 

## Usage

1. Complete one manual checklist.
2. Create the `list` CSV file and add every machine that is a duplicate of that completed system. Ex:
    ```
    machine1,192.168.1.6,38:D5:47:7A:46:B6
    machine2,192.168.1.7,38:D5:47:7A:46:B5
    machine3,192.168.1.8,38:D5:47:7A:46:B4
    machine4,192.168.1.9,38:D5:47:7A:46:B3
    testbox,192.168.1.10,38:D5:47:7A:46:B2
    mehljbox,192.168.1.11,38:D5:47:7A:46:B1
    ```
3. Run the script, specifying both of these files:
    ```
    $ python main.py machines windows10.ckl
    ```
4. The new checklists will be located in your current directory, under `./checklists/`. 
Each checklist will contain the same data as the original completed one, except with unique hostname/MAC/IP info.
    ```
    $ ls ./checklists/
    machine1.ckl machine2.ckl machine3.ckl machine4.ckl testbox.ckl mehljbox.ckl 
    ```