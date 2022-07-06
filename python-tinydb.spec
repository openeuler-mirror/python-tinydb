%global _empty_manifest_terminate_build 0
Name:		python-tinydb
Version:	4.7.0
Release:	1
Summary:	TinyDB is a tiny, document oriented database optimized for your happiness
License:	MIT
URL:		https://github.com/msiemens/tinydb
Source0:	https://files.pythonhosted.org/packages/77/b3/2ab727ab4062800731c2e4d773358c6c25f8d630affa3e3ccdb21dc40d68/tinydb-4.7.0.tar.gz
BuildArch:	noarch

Requires:	python3-typing-extensions

%description
TinyDB is a lightweight document oriented database optimized for your happiness

%package -n python3-tinydb
Summary:	TinyDB is a tiny, document oriented database optimized for your happiness
Provides:	python-tinydb
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-tinydb
TinyDB is a lightweight document oriented database optimized for your happiness

%package help
Summary:	Development documents and examples for tinydb
Provides:	python3-tinydb-doc
%description help
TinyDB is a lightweight document oriented database optimized for your happiness

%prep
%autosetup -n tinydb-4.7.0

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-tinydb -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Jul 07 hkgy <kaguyahatu@outlook.com> - 4.7.0-1
- Upgrade version to 4.7.0

* Wed Sep 22 2021 Python_Bot <Python_Bot@openeuler.org> - 4.5.1-1
- Package Init
