from setuptools import setup, find_packages
    
with open('README.md', encoding='utf-8') as f: # README.md 내용 읽어오기
    long_description = f.read()

setup(
    name                = 'video_dataloader_for_pytorch',
    version             = '0.1',
    long_description    = long_description,          # readme
    long_description_content_type = 'text/markdown', # markdown
    description         = 'A small example package',
    author              = 'hossay',
    author_email        = 'youhs4554@gmail.com',
    url                 = 'https://github.com/youhs4554/video-dataloader-pytorch.git', # github url
    download_url        = 'https://github.com/youhs4554/video-dataloader-pytorch/archive/refs/tags/v0.1.tar.gz', # release url
    install_requires    =  ["torch", "torchvision", "scikit-learn", "decord", "matplotlib", "einops", "natsort", "pandas"], # required packages
    packages            = find_packages(exclude = []),
    keywords            = ['video tool', 'pytorch'], # 키워드
    python_requires     = '>=3.6', # python 필요 버전
    package_data        = {}, 
    zip_safe            = False,
    classifiers         = [   
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)