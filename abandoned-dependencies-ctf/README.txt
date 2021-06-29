Abandoned Dependencies CTF
--------------------------
- From the abandoned-dependencies-ctf directory, build the docker image:
    - docker build --no-cache -t img .

- Now run the image:
    - docker run -it test

- Now open another shell/terminal, and create a file named server.py with the code from the "misc_1.txt" file. NOTE: The host ip here must be set to the IP of your local machine

- In this second shell, navigate to a desired directory and clone the "password" github repo:
    - git clone https://github.com/huy26/password.git

- In password.py, add the code from "misc_2.txt". NOTE: Add the import statement at the top. Add the rest of  the code after the while loop but before the return statement, with proper indentation of course. Also, the host ip here, like in misc_1, must be set to the IP of your local machine. 

- Add, commit, and push this code to the "password" repo:

- Start the server.py file

- In the first shell, rebuild and rerun as in steps 1 & 2

- You should see your entered password output in shell 2 by server.py. Now close the server by hitting ctrl + c.

- Now it's time to clean up our changes. In shell 2, undo your changes to the "password" repo:
    - git switch -C <local_branch_name> <remote_name>/<remote_branch_name>~1
    - git push --force

- Finally, delete your local "password" repo in shell 2.
