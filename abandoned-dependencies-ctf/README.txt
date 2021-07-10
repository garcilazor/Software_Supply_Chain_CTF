Abandoned Dependencies CTF
--------------------------
Part 1: Create a personal copy of the package that we will be adding malicious code to later (so that we don't modify the main copy and others can use it as well)
-------------------------------------------------------------------------------------------------------
- Get into the docker image and run it:
    - docker run -it abandoned-dependencies

- Clone this repo:
    - git clone https://github.com/huy26/password.git

- Go into the password folder and remove the current remote
    - git remote remove origin

- Go into your Github account and create a new repo named 'password'

- Add the new repo as a remote
    - git remote add origin https://github.com/${YOUR_USER}/password.git

- Install this package into the image:
    - pip3 install git+https://github.com/${YOUR_USER}/password 

--------------------------------------------------------------------------------------------------
Part 2: Run the main application that utilizes multiple packages, including the one from part 1
-----------------------------------------------------------------------------------------------------------

- Now run the main script:
    - python main.py

--------------------------------------------------------------------------------------------------
Part 3: Set up server on local machine and client in packge from step 1. The client will send info to the server, without the users knowledge
--------------------------------------------------------------------------------------------------------------------
- Open another shell, not in the docker image, and create a file named server.py with the code from the "misc_1.txt" file (found in the abandoned-dep folder). NOTE: For this file and the next one, you need to replace the "host" value with your machines ip. Use the command ipconfig (Windows) or ifconfig (Linux), and look for your non-docker ip address. It should be ethernet or wifi. The command "hostname -I" should also give you a list of ip's.

- In the first shell, in password.py of the password repo, add the code from "misc_2.txt" (found in the abandoned-dep folder). NOTE: Add the import statements at the top. Add the rest of  the code after the while loop but before the return statement, with proper indentation of course. Also, in setup.py of the password repo, change the version from 0.1 to 0.2.

- Add, commit, and push this code to the "password" repo you created

- Re-install the password package
    - pip3 install git+https://github.com/${YOUR_USER}/password 

--------------------------------------------------------------------------------------------------
Part 4: Run the main application again, this time with one of its packages having malicious code
--------------------------------------------------------------------------------------------------
- Start the server.py file in the second shell

- In the first shell, rerun as in part 2

- You should see your entered password output in shell 2 by server.py. Now close the server by hitting ctrl + c.

- Exit the docker container with the command "exit" 

- Delete your remote password github repo if desired
