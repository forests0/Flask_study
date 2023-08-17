import os
import openai
openai.organization = "org-Gpua4wwbFGkOOtbuKYhOTlrH"
openai.api_key = os.getenv("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")
openai.Model.list()

# {
#    "id":"chatcmpl-abc123",
#    "object":"chat.completion",
#    "created":1677858242,
#    "model":"gpt-3.5-turbo-0301",
#    "usage":{
#       "prompt_tokens":13,
#       "completion_tokens":7,
#       "total_tokens":20
#    },
#    "choices":[
#       {
#          "message":{
#             "role":"assistant",
#             "content":"\n\nThis is a test!"
#          },
#          "finish_reason":"stop",
#          "index":0
#       }
#    ]
# }