# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    "requests>=2.17.0"
]

setup(
    name="ai_agent_directory",   # Required
    version="0.0.3",    # Required
    description="AI Agent Directory AI Agent Directory to Host All AI Agent Directory related AI Agents Services, Community, Reviews and More.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="AI Agent Hub",
    author_email="dingo0927@126.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="AI Agent Directory, AI Agent Marketplace,AI Agent Directory,AI Agents,Agentic AI",
    packages=find_packages(where="src"),  # Required
    install_requires=install_requires,    # Required    
    package_data={'ai_agent_directory': ['*.txt', '*.json']
        , 'ai_agent_directory.data': ['*.txt', '*.json']
    },    
    package_dir={"": "src"},
    python_requires=">=3.4",
    project_urls={
        "homepage": "http://www.deepnlp.org/store/ai-agent",
        "repository": "https://github.com/AI-Agent-Hub/AI-Agent-Directory"
    },
)
