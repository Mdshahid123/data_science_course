error_response={
  'error': {'message': 'Insufficient Balance', 'type': 'unknown_error', 'param': None, 'code': 'invalid_request_error'
    }
}

print(error_response)
print(error_response["error"]["message"])