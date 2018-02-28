{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "import requests, json, time\n",
    "\n",
    "def send_slack(msg):\n",
    "\n",
    "# 슬랙 웹훅 URL\n",
    "    webhook_URL = \"https://hooks.slack.com/services/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\"\n",
    "# 데이터 \n",
    "    data = {\n",
    "    \"channel\": \"#webhook\", \"emoji\": \":angry:\", \"msg\": msg, \"username\": \"매니져\",\n",
    "    }\n",
    "# 페이로드 생성 \n",
    "    payload = {\n",
    "    \"channel\": data[\"channel\"], \"username\": data[\"username\"], \"icon_emoji\": data[\"emoji\"], \"text\": data[\"msg\"],\n",
    "    }\n",
    "# 전송\n",
    "    response = requests.post(\n",
    "    webhook_URL,\n",
    "    data = json.dumps(payload), )\n",
    "\n",
    "# 결과 print(response)\n",
    "s = datetime.datetime.now() \n",
    "send_slack(str(s))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
