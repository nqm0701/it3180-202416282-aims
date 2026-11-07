# Lab 03 - Câu hỏi thảo luận

## 1. Merge base là gì?
Merge base là commit tổ tiên chung gần nhất của hai nhánh, tức là điểm
hai nhánh bắt đầu tách ra (xem bằng `git merge-base A B`). Khi merge, Git
dùng 3-way merge với ba phiên bản: merge base, đầu nhánh hiện tại và đầu
nhánh được merge vào. Với mỗi vùng mã, nếu chỉ một bên thay đổi so với
merge base thì lấy bên đó; nếu cả hai bên cùng sửa một vùng theo cách khác
nhau thì phát sinh xung đột và phải giải quyết thủ công. Merge base càng cũ
thì khả năng xung đột càng cao, vì vậy nên giữ nhánh sống ngắn và đồng bộ
với master thường xuyên.

## 2. Vì sao master và release/* phải dùng revert?
master và release/* là lịch sử chung, nhiều người và nhiều nhánh đã dùng
làm nền. `git reset` hoặc rebase viết lại lịch sử bằng SHA mới, làm lịch
sử của người khác bị lệch so với remote, phải force push mới đẩy được
(có thể đè mất commit của người khác) và bị branch protection chặn. Reset
cũng làm mất dấu vết thay đổi, trong khi SCM yêu cầu truy vết được ai thay
đổi gì và vì sao. `git revert` không viết lại lịch sử: nó tạo một commit
mới đảo ngược thay đổi cũ, nên lịch sử chỉ tiến về phía trước, an toàn,
truy vết được và đi qua PR như mọi thay đổi khác. Khi revert một merge
commit cần `-m 1` để chọn nhánh cha thứ nhất (master) làm mainline.
