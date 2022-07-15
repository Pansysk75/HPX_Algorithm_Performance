import math
import os
from pathlib import Path
import subprocess
import progressbar as pb
import pandas as pd
import numpy as np


def run_speedup_test(executable_path: Path, n_max):
    cpu_count = os.cpu_count()
    data = pd.DataFrame()
    data["n"] = [int(n) for n in np.logspace(0, math.log10(n_max), 50)]

    for executable in executable_path.iterdir():
        result = single_run_speedup_test(
            executable, data["n"].to_list())
        data[executable.stem] = result

    data.set_index("n", inplace=True)

    alg_name = executable_path.name
    save_path = "./results/speedup_test/" + alg_name + "/"
    file_name = alg_name + "(n_max=10^" + str(int(math.log10(n_max))) + ").csv"
    Path(save_path).mkdir(parents=True, exist_ok=True)
    data.to_csv(save_path + file_name)


def single_run_speedup_test(executable_path: Path, n_list):
    print("Starting speedup run (" + executable_path.name + "):")

    data = list()
    for n in pb.progressbar(n_list):
        iterations = int(max(1, min(10**8/n, 10**4)))
        command = [executable_path, str(n), str(iterations)]
        output = subprocess.run(command, capture_output=True)
        data.append(float(output.stdout))

    print("Run finished\n")
    return data


def run_weak_scaling(executable_path: Path, n_max):
    cpu_count = os.cpu_count()
    data = pd.DataFrame()
    data["cores"] = range(1, cpu_count+1)
    data["n"] = data["cores"]*n_max/data["cores"].max()

    cores_n_list = list(data.itertuples(index=False, name=None))

    for executable in executable_path.iterdir():
        if executable.stem == "std_seq":
            continue
        if executable.stem == "std_par":
            continue
        result = single_run_weak_scaling(
            executable, cores_n_list)
        data[executable.stem] = result

    data.set_index("cores", inplace=True)

    alg_name = executable_path.name
    save_path = "./results/weak_scaling/" + alg_name + "/"
    file_name = alg_name + "(n_max=10^" + str(int(math.log10(n_max))) + ").csv"
    Path(save_path).mkdir(parents=True, exist_ok=True)
    data.to_csv(save_path + file_name)


def single_run_weak_scaling(executable_path: Path, cores_n_list):
    print("Starting weak scaling run (" + executable_path.as_posix() + "):")

    data = list()
    for cores, n in pb.progressbar(cores_n_list):
        iterations = int(max(1, min(10**8/n, 10**4)))
        command = [executable_path, str(n), str(iterations),
                   "--hpx:threads="+str(cores)]
        output = subprocess.run(command, capture_output=True)
        data.append(float(output.stdout))
    print("Run finished\n")

    return data


def run_strong_scaling(executable_path: Path, n):
    cpu_count = os.cpu_count()
    data = pd.DataFrame()
    data["cores"] = range(1, cpu_count+1)

    for executable in executable_path.iterdir():
        if executable.stem == "std_seq":
            continue
        if executable.stem == "std_par":
            continue

        result = single_run_strong_scaling(
            executable, data["cores"].tolist(), n)
        data[executable.stem] = result

    data.set_index("cores", inplace=True)

    alg_name = executable_path.name
    save_path = "./results/strong_scaling/" + alg_name + "/"
    file_name = alg_name + "(n=10^" + str(int(math.log10(n))) + ").csv"
    Path(save_path).mkdir(parents=True, exist_ok=True)
    data.to_csv(save_path + file_name)


def single_run_strong_scaling(executable_path: Path, cores_list, n):
    print("Starting strong scaling run (" + executable_path.as_posix() + "):")
    print("n = ", n)
    iterations = int(max(1, min(10**8/n, 10**4)))

    data = list()
    for cores in pb.progressbar(cores_list):
        command = [executable_path, str(n), str(iterations),
                   "--hpx:threads="+str(cores)]
        output = subprocess.run(command, capture_output=True)
        data.append(float(output.stdout))
    print("Run finished\n")
    return data


folder = Path("install/")

print("Found algorithms: ", [
    item.with_suffix("").name for item in folder.iterdir()])

for subfolder in folder.iterdir():
    print("Found executables: ", [
        item.with_suffix("").name for item in subfolder.iterdir()])
    for n in [10**3, 10**4, 10**5, 10**6, 10**8]:
        run_strong_scaling(subfolder, n)
        run_weak_scaling(subfolder, n)
    run_speedup_test(subfolder, 10**8)
