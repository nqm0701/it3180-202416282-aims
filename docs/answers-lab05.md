# Lab 05 - Câu hỏi thảo luận

## 1. Ưu, nhược điểm của upstream first so với release first?
Release first (mô hình của học phần): sửa lỗi trên nhánh hotfix tạo từ
release rồi cherry-pick về master. Ưu điểm là bản vá đến tay người dùng
nhanh nhất, được kiểm thử đúng trên mã đang chạy thật và không kéo theo các
thay đổi chưa phát hành của master. Nhược điểm là dễ quên lan truyền bản sửa
về master hoặc các dòng release khác, khiến lỗi tái xuất hiện ở bản sau, nên
phải kiểm toán thường xuyên.
Upstream first (mô hình Release Flow của Microsoft): sửa trên master trước
rồi cherry-pick xuống các nhánh release. Ưu điểm là bản sửa luôn có trong
master nên không thể bị quên và mọi bản sau đều chứa nó, review tập trung ở
một nơi. Nhược điểm là chậm hơn khi cần vá khẩn cấp, và vì master đã đi xa
hơn release nên bản sửa có thể phụ thuộc vào thay đổi mới, gây xung đột khi
cherry-pick xuống release.

## 2. Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F phát hiện?
Lệnh `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`
sẽ chỉ trả về một commit (trên master) thay vì hai. Lệnh
`git cherry -v origin/release/lab05 origin/master` sẽ hiện commit sửa lỗi
với dấu "+", nghĩa là release/lab05 chưa có bản tương đương. Ngoài ra vòng
lặp kiểm tra hành vi trên các phiên bản sẽ cho kết quả sai ở v1.1.0.
`git tag --contains <FIX_SHA>` không phát hiện được vì cherry-pick tạo SHA
mới khác với SHA gốc.
