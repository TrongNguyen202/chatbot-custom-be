from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import processpromt
from vertor import answer_pro
from chatbot_option2 import processpromt_option

app = Flask(__name__)

# Cấu hình CORS để cho phép truy cập từ http://127.0.0.1:5500
CORS(app, resources={r"/chat": {"origins": "http://127.0.0.1:5500"}})


@app.route('/chat', methods=['POST'])
def chat():
    try:
        print("dang vao")
        # Lấy dữ liệu JSON từ request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        message_get = data.get("content")

        # Kiểm tra nếu không có tin nhắn
        if not message_get:
            return jsonify({"error": "Content is required"}), 400

        # Xử lý tin nhắn ban đầu
        return_message = processpromt(message_get)
        if not return_message:
            return jsonify({"error": "Error processing prompt"}), 500
        print("return mesage",return_message)
        # Nếu trả lời là "không biết", xử lý tiếp
        if "không biết" in return_message:
            print("Processing further...")  # Debug line
            option2 = answer_pro(message_get)
            # print("option 2", option2)
            # Kiểm tra nếu option2 không rỗng và có ít nhất 2 phần tử
            if not option2 or len(option2) < 2:
                return jsonify({"error": "Option2 is empty or invalid"}), 500

            # Xử lý câu trả lời thứ 2 từ option2
            final_answer = processpromt_option(option2[0])
            print("final_answer",final_answer)
            if not final_answer:
                return jsonify({"error": "Error processing final answer"}), 500

            return jsonify({"response": final_answer})

        # Trả lại câu trả lời bình thường
        return jsonify({"response": return_message})

    except Exception as e:
        # Log lỗi chi tiết
        print(f"Error: {str(e)}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Chạy server tại localhost:5000
if __name__ == '__main__':
    app.run(debug=True)
