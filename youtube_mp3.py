from argparse import ArgumentParser as Parser
import subprocess as sp


def download(URL=''):
    sp.call(f'youtube-dl {URL} -o temp.mp4 -f mp4')
    sp.call('ffmpeg -i temp.mp4 -vn -ac 2 -ar 44100 -ab 256k -acodec libmp3lame -f mp3 output.mp3')


if __name__ == '__main__':
    parser = Parser()
    parser.add_argument('-u', '--URL', type=str, help='Specify URL')
    args = parser.parse_args()
    download(args.URL)
