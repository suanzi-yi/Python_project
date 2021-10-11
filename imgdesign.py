import cv2
import numpy as np

#最近邻插值
def most_near(s):
    m_new = m * a
    m_new = int(m_new)
    n_new = n * a
    n_new = int(n_new)
    T1 = np.zeros(shape=(m_new, n_new))
    for i in range(m_new):
        for j in range(n_new):
            if i/a >= m or j/a >= n:
                T1[i][j]=0
            else:
                T1[i][j]=s[round(i/a)][round(j/a)]
    T1 = T1.astype(np.uint8)  # 进行类型转换
    return T1

#双线性插值
def double_linear(s):
    z=s.astype(float)
    print(z[1][1].dtype)
    m_new = m * a
    m_new = int(m_new)
    n_new = n * a
    n_new = int(n_new)
    T1 = np.zeros(shape=(m_new, n_new))
    for i in range(m_new):
        for j in range(n_new):
            if i / a >= m or j / a >= n or int(i//a)+1>=m or int(j//a)+1>=n:
                T1[i][j] = 0
            else:
                x1 = int(i // a)
                y2 = int(j // a)
                x2 = x1 + 1
                y1 = y2 + 1
                T1[i][j] = ((y2-j/a)/(y2-y1))*((x2-i/a)/(x2-x1)*z[x1][y1] + (i/a-x1)/(x2-x1)*z[x2][y1]) + ((j/a-y1)/(y2-y1))*((x2-i/a)/(x2-x1)*z[x1][y2] + (i/a-x1)/(x2-x1)*z[x2][y2])
    T1 = T1.astype(np.uint8)  # 进行类型转换
    return T1

#双三次插值
def three_linear(s):
    z = s.astype(float)
    # print(z[1][1].dtype)
    aa = -0.5
    m_new = m * a
    m_new = int(m_new)
    n_new = n * a
    n_new = int(n_new)
    T1 = np.zeros(shape=(m_new, n_new))

    for i in range(m_new):
        for j in range(n_new):
            if i / a >= m or j / a >= n or int(i // a) + 2 >= m or int(j // a) + 2 >= n:
                T1[i][j] = 0
            else:
                x1 = int(i // a)
                y1 = int(j // a)
                x0 = x1 - 1
                y0 = y1 - 1
                x2 = x1 + 1
                y2 = y1 + 1
                x3 = x2 + 1
                y3 = y2 + 1
                t001 = np.abs(i / a - x0)
                t002 = np.abs(j / a - y0)
                t101 = np.abs(i / a - x1)
                t102 = np.abs(j / a - y0)
                t201 = np.abs(i / a - x2)
                t202 = np.abs(j / a - y0)
                t301 = np.abs(i / a - x3)
                t302 = np.abs(j / a - y0)
                t011 = np.abs(i / a - x0)
                t012 = np.abs(j / a - y1)
                t021 = np.abs(i / a - x0)
                t022 = np.abs(j / a - y2)
                t031 = np.abs(i / a - x0)
                t032 = np.abs(j / a - y3)
                t111 = np.abs(i / a - x1)
                t112 = np.abs(j / a - y1)
                t211 = np.abs(i / a - x2)
                t212 = np.abs(j / a - y1)
                t311 = np.abs(i / a - x3)
                t312 = np.abs(j / a - y1)
                t121 = np.abs(i / a - x1)
                t122 = np.abs(j / a - y2)
                t221 = np.abs(i / a - x2)
                t222 = np.abs(j / a - y2)
                t321 = np.abs(i / a - x3)
                t322 = np.abs(j / a - y2)
                t131 = np.abs(i / a - x1)
                t132 = np.abs(j / a - y3)
                t231 = np.abs(i / a - x2)
                t232 = np.abs(j / a - y3)
                t331 = np.abs(i / a - x3)
                t332 = np.abs(j / a - y3)
                k11 = ((aa + 2) * pow(t111, 3) - (aa + 3) * pow(t111, 2) + 1) * (
                (aa + 2) * pow(t112, 3) - (aa + 3) * pow(t112, 2) + 1)
                k12 = ((aa + 2) * pow(t121, 3) - (aa + 3) * pow(t121, 2) + 1) * (
                (aa + 2) * pow(t122, 3) - (aa + 3) * pow(t122, 2) + 1)
                k21 = ((aa + 2) * pow(t211, 3) - (aa + 3) * pow(t211, 2) + 1) * (
                (aa + 2) * pow(t212, 3) - (aa + 3) * pow(t212, 2) + 1)
                k22 = ((aa + 2) * pow(t221, 3) - (aa + 3) * pow(t221, 2) + 1) * (
                (aa + 2) * pow(t222, 3) - (aa + 3) * pow(t222, 2) + 1)

                k00=(aa*pow(t001,3)-5*aa*pow(t001,2)+8*aa*t001-4*aa)*(aa*pow(t002,3)-5*aa*pow(t002,2)+8*aa*t002-4*aa)
                k10=(aa*pow(t101,3)-5*aa*pow(t101,2)+8*aa*t101-4*aa)*(aa*pow(t102,3)-5*aa*pow(t102,2)+8*aa*t102-4*aa)
                k20=(aa*pow(t201,3)-5*aa*pow(t201,2)+8*aa*t201-4*aa)*(aa*pow(t202,3)-5*aa*pow(t202,2)+8*aa*t202-4*aa)
                k30=(aa*pow(t301,3)-5*aa*pow(t301,2)+8*aa*t301-4*aa)*(aa*pow(t302,3)-5*aa*pow(t302,2)+8*aa*t302-4*aa)
                k01=(aa*pow(t011,3)-5*aa*pow(t011,2)+8*aa*t011-4*aa)*(aa*pow(t012,3)-5*aa*pow(t012,2)+8*aa*t012-4*aa)
                k31=(aa*pow(t311,3)-5*aa*pow(t311,2)+8*aa*t311-4*aa)*(aa*pow(t312,3)-5*aa*pow(t312,2)+8*aa*t312-4*aa)
                k02=(aa*pow(t021,3)-5*aa*pow(t021,2)+8*aa*t021-4*aa)*(aa*pow(t022,3)-5*aa*pow(t022,2)+8*aa*t022-4*aa)
                k32=(aa*pow(t321,3)-5*aa*pow(t321,2)+8*aa*t321-4*aa)*(aa*pow(t322,3)-5*aa*pow(t322,2)+8*aa*t322-4*aa)
                k03=(aa*pow(t031,3)-5*aa*pow(t031,2)+8*aa*t031-4*aa)*(aa*pow(t032,3)-5*aa*pow(t032,2)+8*aa*t032-4*aa)
                k13=(aa*pow(t131,3)-5*aa*pow(t131,2)+8*aa*t131-4*aa)*(aa*pow(t132,3)-5*aa*pow(t132,2)+8*aa*t132-4*aa)
                k23=(aa*pow(t231,3)-5*aa*pow(t231,2)+8*aa*t231-4*aa)*(aa*pow(t232,3)-5*aa*pow(t232,2)+8*aa*t232-4*aa)
                k33=(aa*pow(t331,3)-5*aa*pow(t331,2)+8*aa*t331-4*aa)*(aa*pow(t332,3)-5*aa*pow(t332,2)+8*aa*t332-4*aa)
                T1[i][j] = z[x0][y0]*k00 + z[x0][y1]*k01 + z[x0][y2]*k02 + z[x0][y3]*k03 + z[x1][y0]*k10 + z[x1][y1]*k11 + z[x1][y2]*k12 + z[x1][y3]*k13 + z[x2][y0]*k20 + z[x2][y1]*k21 + z[x2][y2]*k22 + z[x2][y3]*k23 + z[x3][y0]*k30 + z[x3][y1]*k31 + z[x3][y2]*k32 + z[x3][y3]*k33
    T1 = T1.astype(np.uint8)  # 进行类型转换
    return T1


if __name__=='__main__':
    src = cv2.imread(r"p2.jpg")
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    print(gray)
    m, n = gray.shape
    m = int(m)
    n = int(n)
    print(m, n)
    a = 1.5
    cv2.imshow('init', gray)
    cv2.imshow('most_nar',most_near(gray))
    cv2.imshow('double_linear',double_linear(gray))
    cv2.imshow('three_linear',three_linear(gray))
    cv2.waitKey(0)
