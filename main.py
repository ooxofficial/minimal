import os

print("Welcome to Minimal 1.0!")
print("Enter the file you want to compile")
root = input("> ")

if root.endswith(".min"):
    if os.path.exists(root):
        with open(root, "r") as f:
            fval = f.read().strip()

            if 'print("' in fval and '")' in fval:
                start_index = fval.find('"') + 1
                end_index = fval.rfind('"')
                printval = fval[start_index:end_index]

                with open("main.c", "w") as f:
                    f.write("""
                    #include <stdio.h>

                    int main() {{
                        printf("%s", "{}");
                        return 0;
                    }}
                    """.format(printval))

                os.system("gcc main.c -o main.exe")
                os.remove("main.c")
            else:
                print("Invalid function in " + root)
    else:
        print("File does not exist")
else:
    print("Invalid file format")
