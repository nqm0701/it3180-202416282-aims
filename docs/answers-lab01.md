# Lab 01 - Câu hỏi thảo luận

## 1. Cấu hình --global được lưu ở đâu? Khác gì so với --local?
`--global` lưu trong `~/.gitconfig` và áp dụng cho mọi repo của người dùng.
`--local` lưu trong `.git/config` của từng repo, chỉ áp dụng cho repo đó
và được ưu tiên hơn `--global`.

## 2. Vì sao dùng git mv?
`git mv` giúp Git nhận ra đây là thao tác đổi tên/di chuyển chứ không phải
xóa rồi thêm tệp mới. Nhờ đó PR hiển thị "renamed" và `git log --follow`
vẫn truy được lịch sử cũ của tệp.

## 3. release/lab01 có phải baseline không?
Có. Đó là phiên bản đã được thống nhất và đóng băng để nộp bài,
chỉ thay đổi qua quy trình (PR, hotfix), đúng định nghĩa baseline trong SCM.

## 4. Vì sao không commit thẳng master dù làm một mình?
Để có dấu vết truy vết (PR, mô tả, review), có điểm kiểm soát trước khi
tích hợp, và rèn đúng quy trình như khi làm nhóm.
