# Lab 04 - Câu hỏi thảo luận

## 1. Vì sao release/* không merge vào master? So sánh với GitFlow
release/* là baseline đã đóng băng, chỉ dùng để phát hành và bảo trì bản
đó, còn master tiếp tục phát triển các tính năng mới chưa phát hành. Nếu
merge release ngược vào master, các thay đổi riêng của dòng release (số
phiên bản 1.0.1, bản vá) sẽ lẫn vào master, gây xung đột và làm mờ ranh
giới giữa mã đang phát triển và mã đã phát hành. Bản sửa lỗi được lan
truyền có kiểm soát bằng `cherry-pick -x`, nhờ đó truy vết được nguồn gốc
từng bản sửa. GitFlow có hai nhánh dài hạn là main và develop, còn release/*
và hotfix/* đều merge ngược về cả main lẫn develop. Mô hình của học phần chỉ
có master làm nhánh phát triển duy nhất, release/* là nhánh bảo trì không
merge ngược, nên ít nhánh dài hạn hơn và dễ duy trì nhiều phiên bản song song.

## 2. Vì sao lên 1.0.0 mà không phải 0.4.0?
Theo Semantic Versioning, các bản 0.y.z là giai đoạn phát triển ban đầu,
chưa ổn định và API có thể thay đổi bất cứ lúc nào. 1.0.0 đánh dấu bản
phát hành chính thức đầu tiên, tuyên bố API công khai đã ổn định. Sau Lab
01-03 sản phẩm đã có đủ tính năng cơ bản, có test và đã sửa lỗi nên được
coi là bản ổn định đầu tiên. Từ 1.0.0, mọi thay đổi phải tuân theo quy tắc
MAJOR (phá vỡ tương thích), MINOR (thêm tính năng tương thích) và PATCH
(chỉ sửa lỗi).
