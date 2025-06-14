import argparse
from azul.process_reporter import get_processes, save_report


def main():
    parser = argparse.ArgumentParser(
        description="Azul Project - Process Reporter CLI")
    parser.add_argument(
        '--format', choices=['csv', 'json'], default='csv', help="Output format")
    parser.add_argument('--output', default='azul_process_report',
                        help="Output filename without extension")
    args = parser.parse_args()

    data = get_processes()
    save_report(data, args.format, args.output)
    print(f"Report saved as {args.output}.{args.format}")


if __name__ == '__main__':
    main()
