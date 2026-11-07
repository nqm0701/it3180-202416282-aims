# Lab 02 - Câu hỏi thảo luận

## 1. Vì sao phải đồng bộ master trước khi tạo PR?
Nhánh tính năng được tạo từ master cũ, trong lúc đó master đã có thêm
thay đổi từ người khác. Merge master vào nhánh trước khi PR giúp phát hiện
và giải quyết xung đột ngay trên nhánh của mình, chạy lại chương trình/test
trên mã đã tích hợp để chắc chắn không làm hỏng master, và giúp PR gọn,
dễ review. Nhờ vậy thứ được duyệt chính là thứ sẽ được tích hợp.

## 2. Khi nào không được rebase?
Không rebase trên commit đã được chia sẻ (đã push và người khác đã
dùng, hoặc là master/release/*), vì rebase viết lại lịch sử bằng các
SHA mới, làm lịch sử của người khác bị lệch và gây xung đột khi đồng bộ.
Chỉ rebase nhánh riêng, commit chưa chia sẻ.

## 3. feature/* khác topic/* ra sao?
feature/* dùng cho tính năng mới của sản phẩm (thay đổi hành vi của mã
nguồn, ví dụ print_cart, search_by_title). topic/* dùng cho các chủ đề
không phải tính năng, như tài liệu, template, cấu hình
(ví dụ pr-template, use-case-diagram).
