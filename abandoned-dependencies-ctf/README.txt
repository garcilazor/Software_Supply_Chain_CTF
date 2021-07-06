Abandoned Dependencies CTF
--------------------------
Part 1: Create a personal copy of the package that we will be adding malicious code to later (so that we don't modify the main copy and others can use it as well)
-------------------------------------------------------------------------------------------------------
- Clone this repo:
    - git clone https://github.com/huy26/password.git

- Go into the password folder and remove the current remote
    - git remote remove origin

- Go into your Github account and create a new repo named 'password'

- Add the new repo as a remote
    - git remote add origin https://github.com/${YOUR_USER}/password.git

--------------------------------------------------------------------------------------------------
Part 2: Build and run the main application that utilizes multiple packages, including the one from part 1
-----------------------------------------------------------------------------------------------------------
- Now open another shell, and from the abandoned-dependencies-ctf directory, build the docker image:
    - docker build --no-cache --build-arg malicious_pkg=git+https://github.com/${YOUR_USER}/password -t img .

- Now run the image:
    - docker run -it img

--------------------------------------------------------------------------------------------------
Part 3: Set up server on local machine and client in packge from step 1. The client will send info to the server, without the users knowledge
--------------------------------------------------------------------------------------------------------------------
- In the first shell, and create a file named server.py with the code from the "misc_1.txt" file (found in the abandoned-dep folder). NOTE: The host ip here must be set to the IP of your local machine

- In the first shell, in password.py of the password repo, add the code from "misc_2.txt" (found in the abandoned-dep folder). NOTE: Add the import statement at the top. Add the rest of  the code after the while loop but before the return statement, with proper indentation of course. Also, the host ip here, like in misc_1, must be set to the IP of your local machine. 

- NOTE: If the client or server give you any issues with connecting in part 4 below, try the following changes:
    - For server.py, change the host to an empty string ''
    - For password.py, change the host to '0.0.0.0'

- Add, commit, and push this code to the "password" repo you created

--------------------------------------------------------------------------------------------------
Part 4: Run the main application again, this time with one of its packages having malicious code
--------------------------------------------------------------------------------------------------
- Start the server.py file

- In the second shell, rebuild and rerun as in steps 1 & 2

- You should see your entered password output in shell 1 by server.py. Now close the server by hitting ctrl + c.

- Finally, delete your local  and remote "password" repos if desired in shell 1.
