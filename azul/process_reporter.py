import psutil
import json
import csv
import argparse


def get_processes():
    processes = []
    for proc in psutil.process_iter(
        ['pid', 'name', 'username', 'cpu_percent', 'memory_info']
    ):
        try:
            info = proc.info
            info['memory_usage'] = round(
                info['memory_info'].rss / (1024 * 1024), 2
            )  # in MB
            del info['memory_info']
            processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes


def save_report(data, output_format='csv', filename='azul_process_report'):
    if output_format == 'csv':
        with open(f"{filename}.csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    elif output_format == 'json':
        with open(f"{filename}.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    else:
        raise ValueError("Format must be 'csv' or 'json'")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a report of running processes.'
    )
    parser.add_argument(
        '-f',
        '--output-format',
        choices=['csv', 'json'],
        default='csv',
        help='Output format: csv or json'
    )
    parser.add_argument(
        '-o',
        '--output',
        default='azul_process_report',
        help='Output filename (without extension)'
    )

    args = parser.parse_args()

    processes = get_processes()
    save_report(
        processes,
        output_format=args.output_format,
        filename=args.output,
    )
