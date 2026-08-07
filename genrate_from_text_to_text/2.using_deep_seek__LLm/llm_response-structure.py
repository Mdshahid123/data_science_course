act_response={
  "id": "chatcmpl-xxxxxxxx",
  "object": "chat.completion",
  "created": 1754567890,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Large Language Models (LLMs) are AI models trained on massive amounts of text data to understand and generate human-like language."
      },
      "finish_reason": "stop"
    },
  ],
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 24,
    "total_tokens": 36
  }
}

answer=act_response["choices"][0]["message"]["content"]
print(answer)#"Large Language Models (LLMs) are AI models trained on massive amounts of text data to understand and generate human-like language."



# student={
#   "name":"md shahid",
#   "age":24,
#   "address":{
#       "home_no":1234,
#       "strret_no":5
#   }


# }

# my_name=student["name"]
# my_strret=student["address"]["strret_no"]
# print(my_name)
# print(my_strret)






