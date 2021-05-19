#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : QAT_engine
Version  : v0.6.5
Release  : 2
URL      : https://github.com/intel/QAT_Engine/archive/refs/tags/v0.6.5.tar.gz
Source0  : https://github.com/intel/QAT_Engine/archive/refs/tags/v0.6.5.tar.gz
Summary  : Intel QuickAssist Technology (QAT) OpenSSL Engine
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 OpenSSL
Requires: QAT_engine-lib = %{version}-%{release}
Requires: QAT_engine-license = %{version}-%{release}
BuildRequires : intel-ipsec-mb-dev
BuildRequires : ipp-crypto-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libcrypto)

%description
This package provides the Intel QuickAssist Technology OpenSSL Engine
(an OpenSSL Plug-In Engine) which provides cryptographic acceleration
for both hardware and optimized software using Intel QuickAssist Technology
enabled Intel platforms.

%package lib
Summary: lib components for the QAT_engine package.
Group: Libraries
Requires: QAT_engine-license = %{version}-%{release}

%description lib
lib components for the QAT_engine package.


%package license
Summary: license components for the QAT_engine package.
Group: Default

%description license
license components for the QAT_engine package.


%prep
%setup -q -n QAT_Engine-0.6.5
cd %{_builddir}/QAT_Engine-0.6.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621443379
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static --enable-multibuff_offload   --enable-multibuff_ecx  --enable-ipsec_offload --enable-qat_sw
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1621443379
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/QAT_engine
cp %{_builddir}/QAT_Engine-0.6.5/LICENSE %{buildroot}/usr/share/package-licenses/QAT_engine/57f5309a41a66a8f5d057151c44f987757468164
cp %{_builddir}/QAT_Engine-0.6.5/qat/LICENSE.GPL %{buildroot}/usr/share/package-licenses/QAT_engine/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/QAT_Engine-0.6.5/qat_contig_mem/LICENSE.GPL %{buildroot}/usr/share/package-licenses/QAT_engine/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/engines-1.1/qatengine.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/QAT_engine/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/QAT_engine/57f5309a41a66a8f5d057151c44f987757468164
