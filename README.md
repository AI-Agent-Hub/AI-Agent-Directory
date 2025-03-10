# AI Agent Directory AI Agent Directory to Host All AI Agent Directory related AI Agents Web Traffic Data, Search Ranking, Community, Reviews and More.

This is the official github repo for pypi package "ai_agent_directory" https://pypi.org/project/ai_agent_directory. You can use this package to download and get statistics (Google/Bing Search Ranking/Github Stars/Website Traffic) of AI agents on website from AI Agent Marketplace AI Agent Directory and AI Agent Search Portal by Deepnlp AI Agent Marketplace, is the directory for more than 5000+ AI Agents and Apps covering various types of AI agents, such as autonomous agent, chatbots, Computer and Mobile phone use agents, robotic agents, and various industries such as business, finance, law, medical or healthcare, etc. The directory are updated to websites from both public repo (github/huggingface) as well as AI Agent services in cloud service provider (Microsoft Azure AWS, Copilot, GPT Store, Google Cloud, etc). 

### AI Agent Search Engine

Website : http://www.deepnlp.org/search/agent

Find the AI Agent in any category and get the realtime search/app store/github ranking data

![AI Agent Marketplace Directory Search](https://raw.githubusercontent.com/AI-Agent-Hub/AI-Agent-Marketplace/refs/heads/main/AI%20Agent%20Marketplace%20Search.jpg)

Register and list your AI agent For Free through (http://www.deepnlp.org/workspace/my_ai_services)


### AI Agent Directory

Website: http://www.deepnlp.org/store/ai-agent

![AI Agent Marketplace AI Agent Directory](https://raw.githubusercontent.com/AI-Agent-Hub/AI-Agent-Marketplace/refs/heads/main/docs/ai_agents_navigation.jpg)

#### Track Google/Bing Search Ranking Data

For example, if you want to know the AI coding agent traffic data, you can visit (http://www.deepnlp.org/store/ai-agent#section_Coding%20Agent)

You can track vanna.ai, Cody and Cline bot, etc.

- cline bot (http://www.deepnlp.org/store/ai-agent/coding-agent/pub-cline-bot/cline-bot) has google search ranking 37.0 and bing search ranking 15.0, and under search keywords such as "AI Coding Agent, AI Coding, etc.", it got 22.8k Github stars 
- vanna.ai (http://www.deepnlp.org/store/ai-agent/ai-agent/pub-vanna-ai/vanna-ai)
- Cody Sourcegraph (http://www.deepnlp.org/store/ai-agent/ai-agent/pub-cody-by-sourcegraph/cody-by-sourcegraph)
- Taskade.com (http://www.deepnlp.org/store/ai-agent/finance/pub-taskade/taskade)

![AI Coding Agent](https://raw.githubusercontent.com/AI-Agent-Hub/AI-Agent-Marketplace/refs/heads/main/docs/image_coding_agent_v2.jpg)



## API to Track AI Agent Traffic Data

![AI Agent Index for tracking Daily Search Metric](https://raw.githubusercontent.com/AI-Agent-Hub/AI-Agent-Marketplace/refs/heads/main/docs/ai_search_ranking_chart.jpg)

### Install

```
pip install ai_agent_directory

```

### API Seach Agent Web Data Usage
python 

```

import ai_agent_directory as aa
import json

def search_ai_agent_traffic_data():

    result = aa.search(q="Coding Agent Jetbrains")
    print ("## DEBUG: search result is|%s" % str(result))

    result2 = aa.search(q="Coding Agent", limit=20, timeout=5)
    print ("## DEBUG: search result is|%s" % str(result2))

    result3 = aa.search(q="", limit=20, timeout=5)
    print ("## DEBUG: Mock search result is|%s" % str(result3))


search_ai_agent_traffic_data()


```

### API to Add New AI Agent to AI Agent Marketplace | AI Agent Directory | AI Agent Index for Free
You can call the API to register the meta information of your AI Agents. Alternatively, you can also use the web page (http://www.deepnlp.org/workspace/my_ai_services) to list your 
AI Agent.

```

import ai_agent_directory as aa
import json

def publish_your_agent():
    """
        access_key can be obtained from your personal page:
        www.deepnlp.orgworkspace/my_ai_services
        once you submit, it's pending approval and you can track the data then
        get your access_key from http://www.deepnlp.org/workspace/my_ai_services
    """
    access_key = "${your_access_key}"
    name = "My First AI Agent"

    item_info = {}
    item_info["content"] = "This AI Agent can do complicated programming work for humans"
    item_info["website"] = "https://www.my_first_agent.com"
    item_info["field"] = "AI AGENT"
    item_info["subfield"] = "Coding Agent"
    item_info["content_tag_list"] = "coding,python"
    result = aa.add(access_key=access_key, name="My First Agent", item_info=item_info)
    url = result["url"] if "url" in result else ""
    msg = result["msg"] if "msg" in result else ""
    print ("## DEBUG: AI Agent Marketplace Post msg is|%s" % str(msg))
    print ("## DEBUG: AI Agent Marketplace Post url is|%s" % str(url))


publish_your_agent()

```


## GUI Agent

| Types | Year | AGENT NAME | PAPER | PAPER URL | Github  | Website | Demo URL |
| ----- | ----- | ----- |  ------ | ------ | ------ | ------ | ------ |
| GUI Agent | 2024 | OS-ATLAS | OS-ATLAS: A Foundation Action Model For Generalist GUI Agents | https://arxiv.org/pdf/2410.23218  |  https://github.com/OS-Copilot/OS-Atlas?tab=readme-ov-file  |  https://osatlas.github.io/ | - | 
| GUI Agent | 2024 | AutoGLM | AutoGLM: Autonomous Foundation Agents for GUIs | https://arxiv.org/abs/2411.00820 | https://xiao9905.github.io/AutoGLM/ | https://xiao9905.github.io/AutoGLM/ | - |
| GUI Agent | 2024 | EDGE | EDGE: Enhanced Grounded GUI Understanding with Enriched Multi-Granularity Synthetic Data | https://arxiv.org/pdf/2410.19461 | - | - | - |
| GUI Agent | 2024 | FERRET-UI-2 | MASTERING UNIVERSAL USER INTERFACE UNDERSTANDING ACROSS PLATFORMS | https://arxiv.org/pdf/2410.18967 | - | - | - |
| GUI Agent | 2024 | ShowUI | - | - | One vision-language-action model for generalist gui agent | https://arxiv.org/pdf/2411.17465v1 | https://github.com/showlab/ShowUI | - | - |
| GUI Agent | 2024 | Tinyclick | - | - | Tinyclick: Single-turn agent for empowering gui automation | https://arxiv.org/pdf/2410.11871 | https://github.com/SamsungLabs/TinyClick | - | - |
| GUI Agent | 2024 | Openwebvoyager | - | - | Building multimodal web agents via iterative real-world exploration, feedback and optimization. | https://arxiv.org/abs/2410.19609 | - | - | - |
| GUI Agent | 2024 | OSCAR | OPERATING SYSTEM CONTROL VIA STATE-AWARE REASONING AND RE-PLANNING | https://arxiv.org/pdf/2410.18963 | - | - | - |
| GUI Agent | 2024 | PUMA | Large language models empowered personalized web agents. | https://arxiv.org/abs/2410.17236 | - | - | - |
| GUI Agent | 2024 | Agentoccam | A simple yet strong baseline for llm-based web agents | https://arxiv.org/abs/2410.13825 | - | - | - |
| GUI Agent | 2024 | Agent S | Agent s: An open agentic framework that uses computers like a human. | https://arxiv.org/pdf/2410.13825 |  - | - | - |
| GUI Agent | 2024 | Click- agent | Enhancing ui location capabilities of autonomous agents. | https://arxiv.org/abs/2410.11872 | - | - | - |
| GUI Agent | 2024 | LSFS | From Commands to Prompts: LLM-based Semantic File System for AIOS | https://github.com/agiresearch/AIOS-LSFS |  - | - | - |
| GUI Agent | 2024 | Naviqate | Functionality-guided web application navigation | https://arxiv.org/abs/2409.10741 |  - | - | - |
| GUI Agent | 2024 | Periguru | Periguru: A peripheral robotic mobile app operation assistant based on gui image understanding and prompting with llm | https://www.arxiv.org/abs/2409.09354 |  - | - | - |
| GUI Agent | 2024 | Openwebagent | Openwebagent: An open toolkit to enable web agents on large language models. | https://aclanthology.org/2024.acl-demos.8/ |  - | - | - |
| GUI Agent | 2024 | LLMCI | Towards llmci-multimodal ai for llm-vision ui operation. | https://assets-eu.researchsquare.com/files/rs-4653823/v1_covered_70334cd2-05bb-4c26-b0d4-73f9aec48ebc.pdf |  - | - | - |
| GUI Agent | 2024 | Agent-E | From autonomous web navigation to foundational design principles in agentic systems | https://arxiv.org/abs/2407.13032 |  - | - | - |
| GUI Agent | 2024 | Cradle| Empowering foundation agents towards general computer control | https://arxiv.org/abs/2403.03186 |  - | - | - |
| GUI Agent | 2024 | CoAT | Android in the zoo: Chain-of-action-thought for gui agents | https://arxiv.org/abs/2403.02713 |  - | - | - |
| GUI Agent | 2024 | Self-MAP | On the multi-turn instruction following for conversational web agents | https://arxiv.org/abs/2402.15057 |  - | - | - |
| GUI Agent | 2024 | OS-Copilot | Os-copilot: Towards generalist computer agents with self-improvement | https://arxiv.org/abs/2402.07456 |  - | - | - |
| GUI Agent | 2024 | Mobile-Agent | Mobile-agent: Autonomous multi-modal mobile device agent with visual perception | https://arxiv.org/abs/2401.16158 |  - | - | - |
| GUI Agent | 2024 | WebVoyager | Webvoyager: Building an end-to-end web agent with large multimodal models | https://arxiv.org/abs/2401.13919 |  - | - | - |
| GUI Agent | 2024 | Mobileagent AIA | MOBILEAGENT: ENHANCING MOBILE CONTROL VIA HUMAN-MACHINE INTERACTION AND SOP INTEGRATION | https://arxiv.org/pdf/2401.04124  |  - | - | - |
| GUI Agent | 2024 | SeeAct | Gpt-4v (ision) is a generalist web agent, if grounded. | https://arxiv.org/abs/2401.01614 | https://github.com/OSU-NLP-Group/SeeAct |  - | - |
| GUI Agent | 2023 | AppAgent | Appagent: Multimodal agents as smartphone users. | https://arxiv.org/abs/2312.13771 | - | - | - |
| GUI Agent | 2023 | ACE | Assistgui: Task-oriented desktop graphical user interface automation | https://arxiv.org/abs/2312.13771 | - | - | - |
| GUI Agent | 2023 | MobileGPT | Explore, select, derive, and recall: Augmenting llm with human-like memory for mobile task automation. | https://arxiv.org/abs/2312.03003 | https://mobile-gpt.github.io/ | - | - |
| GUI Agent | 2023 | MM-Navigator | Gpt-4v in wonderland: Large multimodal models for zero-shot smartphone gui navigation. | https://arxiv.org/pdf/2311.07562 | - | - | - |
| GUI Agent | 2023 | Webwise | Webwise: Web interface control and sequential exploration with large language models. | https://arxiv.org/abs/2310.16042 | - | - | - |
| GUI Agent | 2023 | Laser | Laser: Llm agent with state-space exploration for web navigation | https://arxiv.org/abs/2309.08172 | - | - | - |
| GUI Agent | 2023 | Synapse | Trajectory-as-exemplar prompting with memory for computer control. | https://arxiv.org/pdf/2306.07863 | - |- | - |
| GUI Agent | 2023 | SheetCopilot | Sheetcopilot: Bringing software productivity to the next level through large language models. | https://arxiv.org/abs/2305.19308 | - |- | - |
| GUI Agent | 2023 | RCI | Language models can solve computer tasks | https://arxiv.org/abs/2303.17491 | - |- | - |
| GUI Agent | 2023 | mobile UIs | Enabling conversational interaction with mobile ui using large language models. | https://arxiv.org/abs/2209.08655 | - | - | - |

### AI Agent in Healthcare

| Application  | AI Agent| Description   |
|  ----  | ----  | ----  |
|  Clinical Decision Support  | [IBM Watson Health](https://www.ibm.com/industries/healthcare) |  Helps analyze medical literature and patient data to provide evidence-based treatment recommendations. | 
|  Clinical Decision Support  | [Infermedica](https://infermedica.com/) |  Provides diagnostic support and triage for healthcare professionals. | 
|  Clinical Decision Support  | [Buoy Health](https://www.buoyhealth.com/) |  A chatbot for symptom checking and guiding users to appropriate care. | 
|  Virtual Health Assistants  | [Ada Health](https://ada.com/) |  Symptom checker and health assessment app with AI-driven insights. | 
|  Virtual Health Assistants  | [Babylon Health](https://en.wikipedia.org/wiki/Babylon_Health) |  Provides symptom checks, virtual consultations, and health monitoring tools. | 
|  Virtual Health Assistants  | [Sensely](https://apps.apple.com/us/app/sensely/id871632284) |  A virtual assistant for managing chronic conditions and improving patient engagement. | 
|  Patient Management  | [HealthTap](https://www.healthtap.com/telehealth/) |  Offers virtual doctor consultations and AI-based symptom checking. | 
|  Patient Management  | [Ginger](https://my.ginger.com/) |  Mental health AI for providing chat-based therapy and support. | 
|  Medical Imaging and Diagnostics  | [Aidoc](https://www.aidoc.com/) |  AI-powered imaging analysis for detecting anomalies in radiology scans. | 
|  Medical Imaging and Diagnostics  | [Zebra Medical Vision](https://www.zebra.cn/cn/zh/solutions.html) |  Automates the analysis of medical imaging data for early detection of diseases. | 
|  Medical Imaging and Diagnostics  | [Arterys](https://www.arterys.com/) |  Uses AI for advanced imaging in cardiology, oncology, and other specialties. | 
|  Drug Discovery and Development  | [Atomwise](https://www.atomwise.com/) |  AI-driven platform for discovering potential drug compounds. | 
|  Drug Discovery and Development  | [BenevolentAI](https://www.benevolent.com/) |  Combines AI and biomedical data to accelerate drug discovery. | 
|  Drug Discovery and Development  | [DeepMind (AlphaFold)](https://deepmind.google/technologies/alphafold/) |  Revolutionizes protein folding predictions for pharmaceutical research. | 
|  Mental Health and Therapy  |  [Woebot](https://woebothealth.com/) |  A chatbot offering cognitive behavioral therapy (CBT) for anxiety and depression. | 
|  Mental Health and Therapy  |  [Replika](https://replika.com/) |  Acts as a conversational agent for emotional support and companionship. | 
|  Mental Health and Therapy  |  [Wysa](https://www.wysa.com/) |  AI for mental health assistance, focusing on stress and emotional well-being. | 
|  Personalized Medicine  |  [23andMe AI](https://therapeutics.23andme.com/our-platform/) |  Uses genetic data to provide personalized health insights and risk assessments. | 
|  Personalized Medicine  |  [Tempus](https://www.tempus.com/) |  Employs AI to personalize cancer treatments based on genetic and molecular data. | 
|  Chronic Disease Management  |  [Livongo](https://www.livongo.com/) |  Combines AI with connected devices for managing diabetes, hypertension, and weight loss. | 
|  Chronic Disease Management  |  [Omada Health](https://www.omadahealth.com/) |  AI-based coaching for chronic disease prevention and management. | 
|  Elderly Care and Accessibility |  [EllieQ by Intuition Robotics](https://elliq.com/) |  AI companion for reducing loneliness and enhancing quality of life in seniors. | 
|  Elderly Care and Accessibility |  [Paro Robot](https://www.parorobots.com/) | Therapeutic AI robot designed for dementia and Alzheimer’s patients. | 
|  Workflow Optimization |  [DeepScribe](https://www.deepscribe.ai/) | AI-powered medical scribe to automate clinical documentation. | 
|  Workflow Optimization |  [Nuance Dragon Medical](https://www.nuance.com/healthcare/dragon-ai-clinical-solutions.html) | Speech recognition AI for documenting patient encounters. | 


# Reference

OS Agents: A Survey on MLLM-based Agents for General Computing Devices Use

### AI Agent List

### Related
#### AI Agent Marketplace and Search
[AI Agent Marketplace and Search](http://www.deepnlp.org/search/agent) <br>
[AI Robot Search](http://www.deepnlp.org/search/robot) <br>
[Equation and Academic search](http://www.deepnlp.org/search/equation) <br>
[AI & Robot Comprehensive Search](http://www.deepnlp.org/search) <br>
[AI & Robot Question](http://www.deepnlp.org/question) <br>
[AI & Robot Community](http://www.deepnlp.org/community) <br>
##### AI Agent
[AI Agent Marketplace Reviews](http://www.deepnlp.org/store/ai-agent) <br>
[AI Agent Marketplace and Search Portal Reviews 2025](http://www.deepnlp.org/blog/ai-agent-marketplace-and-search-portal-reviews-2025) <br>
[AI Agent Publisher](http://www.deepnlp.org/store/pub?category=ai-agent) <br>
[Microsoft AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-microsoft-ai-agent) <br>
[Claude AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-claude-ai-agent) <br>
[OpenAI AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-openai-ai-agent) <br>
[AgentGPT AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-agentgpt) <br>
[Saleforce AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-salesforce-ai-agent) <br>
[AI Agent Builder Reviews](http://www.deepnlp.org/store/ai-agent/ai-agent-builder) <br>
##### Robotics
[Tesla Cybercab Robotaxi](http://www.deepnlp.org/store/pub/pub-tesla-cybercab) <br>
[Tesla Optimus](http://www.deepnlp.org/store/pub/pub-tesla-optimus) <br>
[Figure AI](http://www.deepnlp.org/store/pub/pub-figure-ai) <br>
#### Equation
[DeepNLP Equation Database](http://www.deepnlp.org/equation) <br>
