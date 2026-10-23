"""Вывод списка ветвей текущего репозитория."""
import subprocess


def branches() -> list[str]:
    """Возвращает список локальных ветвей репозитория."""
    out = subprocess.run(["git", "branch", "--format=%(refname:short)"],
                         capture_output=True, text=True, check=False)
    return [line.strip() for line in out.stdout.splitlines() if line.strip()]


if __name__ == "__main__":
    names = branches()
    print(f"Ветвей в репозитории: {len(names)}")
    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")
