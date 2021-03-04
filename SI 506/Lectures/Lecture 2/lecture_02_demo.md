# LECTURE O2 DEMO

## 1.0 Command sequence

Open `Terminal.app` (macOS) or `Git Bash` (Windows). The terminal session should start in your
home directory (confirm with `pwd`). Download `bash.md` and `cli_scratch.py` files to `~/Downloads`.

### Example sequence of commands

:exclamation: in-class demo may vary from example set of commands

```bash
pwd
ls
cd Documents
cd ..
cd Documents
mkdir umich
mkdir umich/courses
cd umich
ls
cd courses
mkdir si506 si507
ls
mkdir si506/lectures
mkdir si506/assignments
cd si506
ls
pwd
cd ~/Downloads
cat cli_scratch.py
cp cli_scratch.py ../Documents/umich/courses/si506/lectures/cli_scratch.py
mv bash.md ../Documents/umich/courses/si506/lectures/
cd ../Documents/umich/courses/si506/lectures/
ls
mv cli_scratch.py cli.py
cat cli.py
```

## 2.0 VS Code

Switch to VS Code.

1. Open `si506` folder (_File -> Open..._)

2. Create Workspace (_File -> Save Workspace As..._)

   Save `si506.code-workspace` in `si506` directory.

3. Create new folder `lecture_02` in the `si506/lectures` folder

4. Move (drag) `cli.py` into the `lecture_02` folder

5. Move (drag) `bash.md` to `lecture_02` folder

6. Open `bash.md` in preview mode (_right click filename -> Open Preview_)

7. Open second editor pane (click icon upper right)

8. Open `cli.py` in second pane.

9. Click green run button and start terminal session.

10. `cli.py` will print to the screen "I love the command line".
